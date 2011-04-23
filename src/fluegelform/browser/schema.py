from zope.component import adapter
from zope.component import adapts
from zope.interface import implements
from plone.schemaeditor.interfaces import ISchemaModifiedEvent
from plone.schemaeditor.browser.schema.traversal import SchemaContext
from plone.supermodel import serializeSchema

from fluegelform.interfaces import IForm
from fluegelform.interfaces import IFormSchemaContext


class FormSchemaContext(SchemaContext):
    implements(IFormSchemaContext)
    adapts(IForm)

    def __init__(self, context, request):
        schema = context.lookupSchema()
        super(FormSchemaContext, self).__init__(schema, request, name='edit-schema')

        self.form = context


@adapter(IFormSchemaContext, ISchemaModifiedEvent)
def save_schema(schema_context, event):
    schema_context.form.schema_xml = serializeSchema(schema_context.schema)
