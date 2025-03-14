import json

from django.contrib import admin
from django.utils.safestring import mark_safe
from polymorphic.admin import (
    GenericStackedPolymorphicInline, PolymorphicInlineSupportMixin,
)

from time_wizard.conf import (
    TIME_WIZARD_COUNTRIES, TIME_WIZARD_COUNTRY_PROVINCES,
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

    def add_view(self, request, form_url="", extra_context=None):
        extra_context = extra_context or {}
        extra_context.update(self.get_extra_selection_context())
        return super().add_view(
            request,
            form_url=form_url,
            extra_context=extra_context,
        )

    def change_view(self, request, object_id, form_url="", extra_context=None):
        extra_context = extra_context or {}
        extra_context.update(self.get_extra_selection_context())
        return super().change_view(
            request,
            object_id,
            form_url=form_url,
            extra_context=extra_context,
        )

    @classmethod
    def get_extra_selection_context(cls):
        return {
            "countries": mark_safe(
                json.dumps(TIME_WIZARD_COUNTRIES)
            ),
            "country_provinces": mark_safe(
                json.dumps(TIME_WIZARD_COUNTRY_PROVINCES)
            ),
        }


admin.site.register(TimeWizardModel, TimeWizardModelAdmin)
