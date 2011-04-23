from zope.interface import implements
from plone.dexterity.content import Container
from fluegelform.interfaces import IForm
from fluegelform.utils import DEFAULT_MODEL_XML
from fluegelform.utils import load_schema


class InvalidatingProperty(object):
    
    def __init__(self, attr, invalidates_attr):
        self.attr = attr
        self.invalidates_attr = invalidates_attr
    
    def __get__(self, inst, klass):
        return getattr(inst, self.attr)
    
    def __set__(self, inst, value):
        setattr(inst, self.attr, value)
        if hasattr(inst, self.invalidates_attr):
            delattr(inst, self.invalidates_attr)


class Form(Container):
    implements(IForm)
    portal_type = 'fluegelform.form'
    
    _schema_xml = DEFAULT_MODEL_XML
    schema_xml = InvalidatingProperty(
        '_schema_xml',
        invalidates_attr='_v_schema'
        )

    def lookupSchema(self):
        schema = getattr(self, '_v_schema', None)
        if schema is None:
            schema = load_schema(self._schema_xml)
            self._v_schema = schema
        return schema
