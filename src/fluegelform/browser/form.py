from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.cachedescriptors.property import Lazy as lazy_property
from plone.autoform.form import AutoExtensibleForm


class FormView(AutoExtensibleForm):
    template = ViewPageTemplateFile('templates/form_view.pt')

    @lazy_property
    def label(self):
        return self.context.Title()

    @lazy_property
    def description(self):
        return self.context.Description()

    @lazy_property
    def schema(self):
        return self.context.schema

    additionalSchemata = ()

    def __init__(self, context, request):
        # Override to avoid hiding the green border
        super(FormView, self).__init__(context, request)
    
    def updateActions(self):
        # override to re-title save button and remove the cancel button
        super(FormView, self).updateActions()
        self.buttons['save'].title = self.context.submit_label
        if 'cancel' in self.buttons:
            del self.buttons['cancel']
