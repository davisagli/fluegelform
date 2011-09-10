from zope.interface import Interface, Attribute
from plone.schemaeditor.interfaces import ISchemaContext


class IForm(Interface):
    """A TTW-configurable form."""

    schema_xml = Attribute("The XML serialization of the current form schema.")
    schema = Attribute("The current form schema. Loaded from the ``schema_xml`` "
                       "attribute on demand, and cached in a volatile attribute, "
                       "``_v_schema``.")


class IFormSchemaContext(ISchemaContext):
    """A plone.schemaeditor schema editing context associated with a form."""

    form = Attribute("The form whose schema is being edited.")
