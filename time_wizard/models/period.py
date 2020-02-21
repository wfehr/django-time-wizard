from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from polymorphic.models import PolymorphicModel

from time_wizard.models.abstract import (
    AbstractAbsoluteRangePeriod, AbstractHolidayRangePeriod,
)
from time_wizard.workarounds import NON_POLYMORPHIC_CASCADE


class PeriodModel(PolymorphicModel):
    """
    Parent model for custom periods.
    """
    content_type = models.ForeignKey(
        'contenttypes.ContentType',
        on_delete=NON_POLYMORPHIC_CASCADE,
        related_name='periods',
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def contains(self, date_time):
        raise NotImplementedError("Override method in child class!")


class AbsolutePeriodModel(AbstractAbsoluteRangePeriod, PeriodModel):
    """
    Period child model for absolute time ranges from start to end.
    """
    class Meta:
        # TODO: only overriden to avoid a migration, remove when new migration
        # is created anyways
        base_manager_name = 'objects'
        abstract = False


class HolidayRangePeriodModel(AbstractHolidayRangePeriod, PeriodModel):
    """
    Period child model for holiday time ranges. Select a holiday and a range
    before, after or both from this date.
    """
    class Meta:
        # TODO: only overriden to avoid a migration, remove when new migration
        # is created anyways
        base_manager_name = 'objects'
        abstract = False
