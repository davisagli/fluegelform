from Acquisition import aq_base, aq_inner
from z3c.form.interfaces import NOT_CHANGED
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.cachedescriptors.property import Lazy as lazy_property
from zope.component import createObject
from zope.component import getUtility
from plone.dexterity.interfaces import IDexterityFTI
from plone.dexterity.browser.add import DefaultAddForm
from plone.dexterity.utils import addContentToContainer
from fluegelform.utils import get_schema_store


class FormView(DefaultAddForm):
    template = ViewPageTemplateFile('templates/form_view.pt')

    portal_type = 'fluegelform.entry'
    description = u''

    @property
    def label(self):
        return self.context.Title()

    @lazy_property
    def schema(self):
        # XXX use the schema digest from when the form was first loaded,
        # in case the schema is being edited while someone is completing
        # the form
        return self.context.lookupSchema()
    
    additionalSchemata = ()

    def __init__(self, context, request):
        # Override to avoid hiding the green border
        super(DefaultAddForm, self).__init__(context, request)
    
    def create(self, data):
        fti = getUtility(IDexterityFTI, name=self.portal_type)

        form = aq_inner(self.context)
        entry = createObject(fti.factory).__of__(form)
        
        # make sure the current form schema is stored
        # and associated with the new entry
        schema_store = get_schema_store()
        entry.schema_digest = schema_store.add(self.schema)

        # save form data
        # (bypass data manager for speed
        # and to avoid needing to reload the form schema)
        for name, field in self.fields.items():
            if name not in data:
                continue
            if data[name] is NOT_CHANGED:
                continue
            setattr(entry, name, data[name])

        return aq_base(entry)
    
    def add(self, entry):
        form = aq_inner(self.context)
        entry = addContentToContainer(form, entry, checkConstraints=False)
    
    def updateActions(self):
        # override to re-title save button and remove the cancel button
        super(FormView, self).updateActions()
        self.buttons['save'].title = self.context.submit_label
        if 'cancel' in self.buttons:
            del self.buttons['cancel']
