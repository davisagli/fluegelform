from zope.interface import Interface, Attribute
from zope import schema
from plone.app.textfield import RichText
from plone.schemaeditor.interfaces import ISchemaContext
from fluegelform import _


class IForm(Interface):
    """A TTW-configurable form."""

    submit_label = schema.TextLine(
        title = _(u'Submit button label'),
        default = _(u'Submit'),
        )
    
    prologue = RichText(
        title = _(u'Form prologue'),
        description = _(u'This text will be displayed above the form fields.'),
        required = False,
        )
    
    epilogue = RichText(
        title = _(u'Form epilogue'),
        description = _(u'This text will be displayed below the form fields.'),
        required = False,
        )

    schema_xml = Attribute("The XML serialization of the current form schema.")

    def lookupSchema():
        """Loads the current form schema from the XML serialization.
        
        The loaded schema is cached in a volatile attribute, _v_schema.
        """


class IEntry(Interface):
    """An entry submitted via a TTW-configurable form."""
    schema_digest = Attribute("The digest of this entry's schema.")

    def lookupSchema():
        """Retrieves this entry's schema from the schema store."""


class ISchemaStore(Interface):
    """A persistent store for Zope schemas.
    
    Schemas are stored by the digest of their plone.supermodel XML
    serialization.
    """

    def get(digest, default=None):
        """Get a schema by its digest.

        The default is returned if there is no value for the digest.
        """

    def __contains__(schema):
        """Tell if a schema exists in the store."""

    def __delitem__(schema):
        """Delete a schema from the store."""

    def add(schema):
        """Adds the schema to the store and returns its digest."""


class IFormSchemaContext(ISchemaContext):
    """A plone.schemaeditor schema editing context associated with a form."""

    form = Attribute("The form whose schema is being edited.")
