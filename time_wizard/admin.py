from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from polymorphic.admin import (
    PolymorphicInlineSupportMixin, StackedPolymorphicInline,
)
from time_wizard.models import (
    AbsolutePeriodModel, HolidayRangePeriodModel, PeriodModel, TimeWizardModel,
)


class PeriodModelInline(StackedPolymorphicInline):
    class AbsolutePeriodModelInline(StackedPolymorphicInline.Child):
        model = AbsolutePeriodModel

    class HolidayRangePeriodModelInline(StackedPolymorphicInline.Child):
        model = HolidayRangePeriodModel

    model = PeriodModel
    child_inlines = (
        AbsolutePeriodModelInline,
        HolidayRangePeriodModelInline,
    )
    template = 'admin/edit_inline/holiday_stacked.html'


@admin.register(TimeWizardModel)
class PeriodModelAdmin(PolymorphicInlineSupportMixin, admin.ModelAdmin):
    inlines = (PeriodModelInline,)
