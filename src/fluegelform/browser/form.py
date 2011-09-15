from zope.component import getMultiAdapter
from lxml import html
from z3c.form import form, field
from plone.app.blocks.layoutbehavior import ILayoutAware
from plone.app.blocks.utils import xpath1
from repoze.xmliter.utils import getHTMLSerializer


class FormView(form.Form):
    ignoreContext = True
    prefix = ''

    @property
    def fields(self):
        fields = []
        for _, tile in self.context.field_tiles():
            fields.extend(tile.fields())
        return field.Fields(*fields)

    def render(self):
        # Render fields by iterating over the form field tiles, rendering
        # each one, and replacing the tile with the result.
        layout = ILayoutAware(self.context).content
        layoutTree = getHTMLSerializer(layout,
            pretty_print=True, encoding='utf8')
        
        for tileId, tile in self.context.field_tiles(layoutTree.tree):
            # XXX need to include the full Plone view of the field
            widget = self.widgets[tile.id]
            widgetRenderer = getMultiAdapter((widget, self.request), name=u'ploneform-render-widget')
            widgetHtml = widgetRenderer()
            tileTree = html.fromstring(widgetHtml).getroottree()
            tileTarget = xpath1("//*[@id='%s']" % tileId, layoutTree.tree)
            
            if tileTarget is None:
                continue
            
            # clear children, but keep attributes
            oldAttrib = dict(tileTarget.attrib)
            tileTarget.clear()
            tileTarget.attrib.update(oldAttrib)

            # insert tile target with tile body
            tileBody = tileTree.find('body')
            if tileBody is not None:
                tileTarget.text = tileBody.text
                for tileBodyChild in tileBody:
                    tileTarget.append(tileBodyChild)
        
        # TODO:
        # - create form tag
        # - fill in status message
        return str(layoutTree)
