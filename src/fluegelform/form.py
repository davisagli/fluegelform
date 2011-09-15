from lxml import etree
from zope.interface import implements
from plone.dexterity.content import Container
from fluegelform.interfaces import IForm, IFieldTile
from plone.app.blocks.utils import tileXPath
from plone.app.blocks.layoutbehavior import ILayoutAware
import logging

logger = logging.getLogger('fluegelform')


class Form(Container):
    implements(IForm)
    portal_type = 'fluegelform.form'

    def field_tiles(self, tree=None):
        if tree is None:
            layout = ILayoutAware(self).content
            tree = etree.HTML(layout)

        for tileNode in tileXPath(tree):
            tileId = tileNode.get('target', None)
            tileHref = tileNode.get('href', None)
            if tileHref is not None:
                if tileHref.startswith('./'):
                    tileHref = tileHref[2:]
                try:
                    tile = self.restrictedTraverse(tileHref)
                except Exception:
                    logger.exception('Could not render tile %s' % tileHref)
                else:
                    if IFieldTile.providedBy(tile):
                        yield tileId, tile

            # remove the tile link from the head
            tileNode.getparent().remove(tileNode)
