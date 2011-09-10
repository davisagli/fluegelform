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
  - Display thank you page
  - Relay to another form (via redirect or re-POST)
  - Store in collective.table
  - Store as full-fledged Dexterity content
  - Store in RDBMS
  - Store in Salesforce

* Possible new use cases to tackle:

  - Multi-page forms
  - Saving incomplete forms for later
  - Surveys (Invite participants, report on results)
  - Reporting on results

Maybe eventually:

* Easily customizable layout (a la Deco)
