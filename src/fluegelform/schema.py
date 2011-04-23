from zope.interface import implements
from zope.interface.declarations import Implements
from zope.interface.declarations import implementedBy
from zope.interface.declarations import ObjectSpecificationDescriptor
from zope.interface.declarations import getObjectSpecification
from persistent import Persistent
from BTrees.OOBTree import OOBTree
from repoze.lru import lru_cache

from fluegelform.interfaces import ISchemaStore
from fluegelform.utils import digest_schema
from fluegelform.utils import load_schema
from fluegelform.utils import get_schema_store


class SchemaStore(Persistent):
    """A persistent utility which stores schemas keyed by the MD5 digest
    of its supermodel serialization.
    """
    implements(ISchemaStore)
    
    def __init__(self):
        self._data = OOBTree()
    
    @lru_cache(100)
    def get(self, digest):
        """Get a schema by its digest.

        A default schema is returned if there is no value for the digest.
        
        Results are cached in an LRU cache.
        """
        xml = self._data.get(digest, None)
        return load_schema(xml)

    def __contains__(self, schema):
        """Tell if a schema exists in the store."""
        _, digest = digest_schema(schema)
        return digest in self._data

    def __delitem__(self, schema):
        """Delete a schema from the store."""
        _, digest = digest_schema(schema)
        del self._data[digest]

    def add(self, schema):
        """Adds the schema to the store and returns its digest."""
        xml, digest = digest_schema(schema)
        self._data[digest] = xml
        return digest


class SchemaStoreSpecificationDescriptor(ObjectSpecificationDescriptor):
    """Assign an instance of this to an object's __providedBy__ to make it
    dynamically declare that it provides the schema referenced in its
    ``schema_digest`` attribute.
    """

    def __get__(self, inst, cls=None):

        if inst is None:
            return getObjectSpecification(cls)

        spec = getattr(inst, '__provides__', None)
        if spec is None:
            spec = implementedBy(cls)

        digest = getattr(inst, 'schema_digest', None)
        schema_store = get_schema_store()
        schema = schema_store.get(digest)
        spec = Implements(schema, spec)
        return spec
