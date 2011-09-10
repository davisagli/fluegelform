from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.cachedescriptors.property import Lazy as lazy_property
from z3c.form import form
from plone.autoform.form import AutoExtensibleForm


class FormView(AutoExtensibleForm, form.Form):
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

    ignoreContext = True
    additionalSchemata = ()
