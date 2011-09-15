from zope.interface import Interface
from zope import schema
from plone.tiles.interfaces import ITile
from plone.app.page.interfaces import IPage
from fluegelform import _


class IForm(IPage):
    """A TTW-configurable form."""


class IFieldTile(ITile):
    """A tile representing a form field."""

    def fields(self):
        """Called to obtain the schema field(s) represented by this tile.
        """


class IField(Interface):
    """The schema of a form field."""

    title = schema.TextLine(title = _(u'Label'))
    description = schema.TextLine(title = _(u'Help Text'))
