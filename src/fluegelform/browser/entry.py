from zope.cachedescriptors.property import Lazy as lazy_property
from plone.autoform.view import WidgetsView


class EntryView(WidgetsView):

    @lazy_property
    def schema(self):
        return self.context.lookupSchema()
