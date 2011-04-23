Introduction
============

Design goals:

* Similar functionality to PloneFormGen, but with a saner, more modern
  architecture based around the Dexterity schema editor.

* Form submissions are stored as content.

* Multiple revisions of the schema can be stored, and each result knows which
  one it's associated with.

* Pluggable actions on form submission:
  - E-mail
  - Relay to another form (via redirect or re-POST)
  - Store as content in ZODB
  - Store in RDBMS
  - Store in Salesforce
  - Display thank you page

* Possible new use cases to tackle:
  - Multi-page forms
  - Saving incomplete forms for later
  - Surveys (Invite participants, report on results)

Maybe eventually:

* Easily customizable layout (a la Deco)

* Be usable inside Zope or Pyramid.
  - This makes the use of at least z3c.form, and probably zope.schema, an
    anti-pattern.
  - Look at colander / deform?
