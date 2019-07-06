from django.contrib import admin
from polymorphic.admin import (
    GenericStackedPolymorphicInline, PolymorphicInlineSupportMixin,
)

from time_wizard.models import (
    AbsolutePeriodModel, HolidayRangePeriodModel, PeriodModel, TimeWizardModel,
)


class PeriodModelInline(GenericStackedPolymorphicInline):
    class AbsolutePeriodModelInline(GenericStackedPolymorphicInline.Child):
        model = AbsolutePeriodModel

    class HolidayRangePeriodModelInline(GenericStackedPolymorphicInline.Child):
        model = HolidayRangePeriodModel

    model = PeriodModel
    child_inlines = (
        AbsolutePeriodModelInline,
        HolidayRangePeriodModelInline,
    )
    template = 'admin/edit_inline/holiday_stacked.html'


class TimeWizardModelAdmin(PolymorphicInlineSupportMixin, admin.ModelAdmin):
    model = TimeWizardModel
    inlines = [PeriodModelInline]


admin.site.register(TimeWizardModel, TimeWizardModelAdmin)
