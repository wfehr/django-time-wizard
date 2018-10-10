import inspect
import sys

import holidays
from django.conf import settings

countries = []
country_provinces = {}
for i in inspect.getmembers(sys.modules['holidays'], inspect.isclass):
    if issubclass(i[1], holidays.HolidayBase) and len(i[0]) < 4:
        countries.append(i[0])
        provinces_states = getattr(i[1], 'PROVINCES', []) or \
            getattr(i[1], 'STATES', [])
        country_provinces.update({i[0]: provinces_states})


TIME_WIZARD_COUNTRIES = getattr(settings, 'TIME_WIZARD_COUNTRIES', countries)
TIME_WIZARD_COUNTRY_PROVINCES = getattr(settings,
                                        'TIME_WIZARD_COUNTRY_PROVINCES',
                                        country_provinces)
