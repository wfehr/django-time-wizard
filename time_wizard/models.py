import datetime

import holidays
from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from polymorphic.models import PolymorphicModel
from time_wizard.conf import TIME_WIZARD_COUNTRIES
from time_wizard.workarounds import NON_POLYMORPHIC_CASCADE


class TimeWizardModel(models.Model):
    """
    Model for the TimeWizard.
    """
    def copy_relations(self, old_instance):
        # Copy PeriodModels
        for periods in old_instance.periods.all():
            # set pk + id to None: https://stackoverflow.com/a/25852807
            periods.pk = None
            periods.id = None
            periods.container_id = self.id
            periods.save()

    @property
    def is_published(self):
        dt = now()
        periods = PeriodModel.objects.filter(container_id=self.id)
        for p in periods:
            if p.contains(dt):
                return True
        return False

    def __str__(self):
        return ' - '.join([str(s) for s in
                           PeriodModel.objects.filter(container_id=self.id)])


class PeriodModel(PolymorphicModel):
    """
    Parent model for custom periods.
    """
    container = models.ForeignKey(
        TimeWizardModel,
        on_delete=NON_POLYMORPHIC_CASCADE,
        related_name="periods"
    )

    def contains(self, date_time):
        raise NotImplementedError("Override method in child class!")


class AbsolutePeriodModel(PeriodModel):
    """
    Period child model for absolute time ranges from start to end.
    """
    start = models.DateTimeField(
        blank=True,
        null=True,
    )
    end = models.DateTimeField(
        blank=True,
        null=True,
    )

    def contains(self, date_time):
        if self.start and self.start > date_time:
            return False
        if self.end and self.end <= date_time:
            return False
        return True

    def __str__(self):
        return 'Absolute [%s - %s]' % (self.start, self.end)


class HolidayRangePeriodModel(PeriodModel):
    """
    Period child model for holiday time ranges. Select a holiday and a range
    before, after or both from this date.
    """
    time_value = models.PositiveSmallIntegerField(
        default=0,
        help_text=_('Amount of time between this and the selected holiday.'),
    )
    TIME_UNIT_CHOICES = (
        ('1', _('Minute')),
        ('60', _('Hour')),
        ('1440', _('Day')),
        ('10080', _('Week')),
    )
    time_unit = models.CharField(
        blank=True,
        choices=TIME_UNIT_CHOICES,
        max_length=16,
        help_text=_('Unit for the chosen time_value.'),
    )
    RANGE_POSITION_CHOICES = (
        ('before', _('Before')),
        ('after', _('After')),
        ('both', _('Both')),
    )
    range_position = models.CharField(
        blank=True,
        choices=RANGE_POSITION_CHOICES,
        max_length=8,
        help_text=_('Choose if a given time range is either before, after or '
                    'before and after the selected holiday.'),
    )
    start_time = models.TimeField(
        blank=True,
        null=True,
    )
    end_time = models.TimeField(
        blank=True,
        null=True,
    )
    country = models.CharField(
        choices=((c, c) for c in TIME_WIZARD_COUNTRIES),
        max_length=8,
    )
    province = models.CharField(
        blank=True,
        max_length=8,
    )
    holiday = models.CharField(
        max_length=64,
    )

    def contains(self, date_time):
        holiday_cls = getattr(holidays, self.country, False)
        if holiday_cls:
            kwargs = {'years': now().year}
            if self.province:
                kwargs.update({'prov': self.province})
            holiday_dict = holiday_cls(**kwargs)
            selected_date = self._get_selected_holiday_date(holiday_dict)
            if selected_date is not None:
                return self._contains_selected_range(date_time, selected_date)
        return False

    def _get_selected_holiday_date(self, holiday_dict):
        selected_date = None
        for d, n in holiday_dict.items():
            if n == self.holiday:
                selected_date = d
                break
        return selected_date

    def _contains_selected_range(self, date_time, selected_date):
        delta1 = datetime.timedelta(minutes=0)
        delta2 = datetime.timedelta(minutes=0)
        mins = self.time_value * int(self.time_unit) if self.time_unit else 0
        if not self.range_position:
            pass
        elif self.range_position in ['before', 'after']:
            delta1 = datetime.timedelta(minutes=mins * -1)
        elif self.range_position == 'both':
            delta1 = datetime.timedelta(minutes=mins * -1)
            delta2 = datetime.timedelta(minutes=mins * 2)
        date1 = datetime.datetime.combine(
            selected_date + delta1,
            self.start_time.time() if self.start_time else date_time.time())
        date2 = datetime.datetime.combine(
            selected_date + delta2,
            self.end_time.time() if self.end_time else date_time.time())
        date_time = date_time.replace(tzinfo=None)
        if date_time < date1 or date_time > date2:
            return False
        return True

    def __str__(self):
        return 'HolidayRange [%s - %s]' % (self.country, self.holiday)


class TimeWizardMixin(models.Model):
    """
    Mixin to let models have a foreign-key-relation to the TimeWizard. Property
    `is_published` is used to indicate if a TimeWizard is set wether or not
    to show the contents/children.
    """
    time_wizard = models.ForeignKey(
        TimeWizardModel,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True

    @property
    def is_published(self):
        return self.time_wizard.is_published
