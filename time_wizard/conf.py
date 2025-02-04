from django.conf import settings
from holidays.utils import list_supported_countries

_country_provinces = list_supported_countries(include_aliases=False)
_countries = list(_country_provinces.keys())


TIME_WIZARD_COUNTRIES = getattr(settings, 'TIME_WIZARD_COUNTRIES', _countries)
TIME_WIZARD_COUNTRY_PROVINCES = getattr(settings,
                                        'TIME_WIZARD_COUNTRY_PROVINCES',
                                        _country_provinces)
