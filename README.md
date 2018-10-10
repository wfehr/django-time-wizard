# django-time-wizard
Date and time dependend content manipulation.

## Quick start

1. Install using pip:

    ```
    pip install django-time-wizard
    ```

1. Add to your `INSTALLED_APPS`:

    ```
    'time_wizard',
    ```

2. Include the time_wizard admin URLs in your project urls.py:

    ```
    url(^'admin/', include('time_wizard.urls')),
    ```

3. Run `python manage.py migrate` to create the time_wizard models.

## Settings

Django-time-wizard uses the defined `countries` and `provinces`/`states` from
`holidays`. Definitions need to be compatible with `holidays`. You can also
define this yourself for your needs:

    TIME_WIZARD_COUNTRIES = ['US', 'UK', 'DE', ...]
    TIME_WIZARD_COUNTRY_PROVINCES = {'US': ['AL', 'AK', ...], ...}

## Requirements

- django
- django-polymorphic
- holidays

## Tests

Setup your test environment with `virtualenv` and install the requirements
with `pip install .`. Also install `tox` via pip and simply run `tox`.
