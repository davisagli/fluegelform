from zope.interface import implements
from plone.dexterity.content import Container
from plone.supermodel import loadString
from fluegelform.interfaces import IForm
from fluegelform.utils import DEFAULT_MODEL_XML
from fluegelform.utils import InvalidatingProperty


class Form(Container):
    implements(IForm)
    portal_type = 'fluegelform.form'
    
    _schema_xml = DEFAULT_MODEL_XML
    schema_xml = InvalidatingProperty(
        '_schema_xml',
        invalidates_attr='_v_schema'
        )

    @property
    def schema(self):
        schema = getattr(self, '_v_schema', None)
        if schema is None:
            schema = loadString(self._schema_xml).schema
            self._v_schema = schema
        return schema
