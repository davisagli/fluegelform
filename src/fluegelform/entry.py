from DateTime import DateTime
from zope.interface import implements
from plone.dexterity.content import Item
from fluegelform.interfaces import IEntry
from fluegelform.schema import SchemaStoreSpecificationDescriptor
from fluegelform.utils import get_schema_store


class Entry(Item):
    implements(IEntry)
    portal_type = 'fluegelform.entry'
    
    __providedBy__ = SchemaStoreSpecificationDescriptor()
    schema_digest = None

    def __init__(self, id=None, **kw):
        kw['title'] = DateTime().ISO8601()
        super(Entry, self).__init__(id, **kw)
    
    def lookupSchema(self):
        schema_store = get_schema_store()
        return schema_store.get(self.schema_digest)
