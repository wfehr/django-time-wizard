==================
django-time-wizard
==================

Date and time dependend content manipulation.

Quick start
===========

1. Install using pip::

    pip install django-time-wizard

2. Make sure to follow the installation steps for `django-polymorphic`


3. Add to your `INSTALLED_APPS`::

    'polymorphic',
    'time_wizard',

4. Include the time_wizard admin URLs in your project urls.py::

    url(^'admin/', include('time_wizard.urls')),

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

      from time_wizard.mixins import TimeWizardMixin
      ...
      class MyModel(TimeWizardMixin, models.Model):
          ...

* use the `PeriodModelInline` in the `admin`, for example:

  * each model of yours can have different time-settings
  * does not effect your database as it works with a generic relationship
  * example::

      from time_wizard.admin import PeriodModelInline
      from polymorphic.admin import PolymorphicInlineSupportMixin
      ...
      class MyModelAdmin(PolymorphicInlineSupportMixin, admin.ModelAdmin):
          inlines = [PeriodModelInline]
          ...

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
