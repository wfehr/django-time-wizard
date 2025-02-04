from django.contrib import admin
from polymorphic.admin import (
    GenericStackedPolymorphicInline, PolymorphicInlineSupportMixin,
)

from time_wizard.conf import TIME_WIZARD_COUNTRIES
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

    def change_view(self, request, object_id, form_url="", extra_context=None):
        extra_context = extra_context or {}
        extra_context["country_choices"] = TIME_WIZARD_COUNTRIES
        return super().change_view(
            request,
            object_id,
            form_url=form_url,
            extra_context=extra_context,
        )


admin.site.register(TimeWizardModel, TimeWizardModelAdmin)
