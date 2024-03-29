==================
django-time-wizard
==================

Date and time dependent content manipulation.

Quick start
===========

1. Install using pip::

    pip install django-time-wizard

2. Make sure to follow the installation steps for `django-polymorphic`


3. Add to your `INSTALLED_APPS`::

    'polymorphic',
    'time_wizard',

4. Include the time_wizard admin URLs in your project urls.py::

    path('admin/', include('time_wizard.urls')),

5. Run `python manage.py migrate` to create the time_wizard models.

Note
====

Upgrading from version `0.2.0` to `1.0.0` will delete all the created  models
of `time_wizard`!

Usage
=====

You can use the `TimeWizard` in different ways:

* use a `ForeignKey`-relation

  * use one `TimeWizardModel`-definition for as much models as you want
  * affects your database as the relation needs a new model field
  * example::

      # models.py
      from time_wizard.mixins import TimeWizardMixin
      ...
      class MyModel(TimeWizardMixin, models.Model):
          ...

* use the `PeriodModelInline` in the `admin`

  * each model of yours can have different time-settings
  * does not affect your database as it works with a generic relationship
  * example::

      # models.py
      from time_wizard.mixins import TimeWizardInlineMixin
      ...
      class MyModel(TimeWizardInlineMixin, models.Model):
          ...

      # admin.py
      from time_wizard.admin import PeriodModelInline
      from polymorphic.admin import PolymorphicInlineSupportMixin
      ...
      class MyModelAdmin(PolymorphicInlineSupportMixin, admin.ModelAdmin):
          inlines = [PeriodModelInline]
          ...

* in both ways use `is_published` on your model to indicate if the content
  is shown or not.

* create a custom `PeriodModel` as a base for custom
  `AbsoluteRange`- and `HolidayRange`-models. There are abstract base classes
  defined in `models/abstract.py`. This means you could for example create
  classes without a generic relation, as `PeriodModel` itself has.

Settings
========

Django-time-wizard uses the defined `countries` and `provinces`/`states` from
`holidays`. Definitions need to be compatible with `holidays`. You can also
define this yourself for your needs::

    TIME_WIZARD_COUNTRIES = ['US', 'UK', 'DE', ...]
    TIME_WIZARD_COUNTRY_PROVINCES = {'US': ['AL', 'AK', ...], ...}

Requirements
============

- django
- django-polymorphic
- holidays

Tests
=====

Setup your test environment with `virtualenv` and install the requirements
with `pip install .`. Also install `tox` via pip and simply run `tox`.

Tests can also be run via `devtools/run-tests`. This requires an environment
where `docker` and `docker-compose` are installed.
