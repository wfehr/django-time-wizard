import holidays
from django.shortcuts import render
from django.utils.timezone import now

from time_wizard.conf import TIME_WIZARD_COUNTRY_PROVINCES


def load_holidays(request):
    country = request.GET.get('country', '')
    province = request.GET.get('province', '')
    holiday_cls = getattr(holidays, country, False)
    context = {}
    if holiday_cls is not False:
        kwargs = {'years': now().year}
        if province:
            kwargs.update({'prov': province})
        context.update({'holidays': holiday_cls(**kwargs)})
    t = 'time_wizard/time_wizard_holiday_range_list_options.html'
    return render(request, t, context)


def load_provinces(request):
    country = request.GET.get('country', '')
    context = {}
    if country in TIME_WIZARD_COUNTRY_PROVINCES:
        context.update({'provinces': TIME_WIZARD_COUNTRY_PROVINCES[country]})
    t = 'time_wizard/time_wizard_province_range_list_options.html'
    return render(request, t, context)
