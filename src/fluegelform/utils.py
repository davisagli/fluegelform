import pkg_resources
from hashlib import md5
from zope.component import getUtility
from plone.supermodel import serializeSchema
from plone.supermodel import loadString
from fluegelform.interfaces import ISchemaStore


DEFAULT_MODEL_XML = pkg_resources.resource_string(
    'fluegelform',
    'models/default_form.xml'
    )


def get_schema_store():
    return getUtility(ISchemaStore)


def digest_schema(schema):
    xml = serializeSchema(schema)
    digest = md5(xml.strip()).hexdigest()
    return xml, digest


def load_schema(xml):
    if xml is None or not xml.strip():
        xml = DEFAULT_MODEL_XML
    return loadString(xml).schema
