from zope import schema
from zope.interface import implements
from z3c.form import form, field
from plone.tiles.tile import PersistentTile
from fluegelform.interfaces import IFieldTile


class FieldTile(PersistentTile):
    implements(IFieldTile)
    field_class = NotImplemented
    
    def fields(self):
        return [self.field_class(__name__=self.id, **self.data)]

    def __call__(self):
        # Render widget(s) for preview in Deco editor
        f = form.Form(self.context, self.request)
        f.ignoreContext = True
        f.ignoreRequest = True
        f.fields = field.Fields(*self.fields())
        f.update()
        return f.render()


class TextLineTile(FieldTile):
    field_class = schema.TextLine
