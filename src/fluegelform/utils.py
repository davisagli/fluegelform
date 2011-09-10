import pkg_resources


DEFAULT_MODEL_XML = pkg_resources.resource_string(
    'fluegelform',
    'models/default_form.xml'
    )


class InvalidatingProperty(object):
    """A property that deletes another attribute when set."""

    def __init__(self, attr, invalidates_attr):
        self.attr = attr
        self.invalidates_attr = invalidates_attr

    def __get__(self, inst, klass):
        return getattr(inst, self.attr)

    def __set__(self, inst, value):
        setattr(inst, self.attr, value)
        if hasattr(inst, self.invalidates_attr):
            delattr(inst, self.invalidates_attr)
