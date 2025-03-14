import datetime

import holidays
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from django.utils.timezone import now

from time_wizard.models import (
    AbsolutePeriodModel, HolidayRangePeriodModel, TimeWizardModel,
)


class TestTimeWizardModel(TestCase):

    def setUp(self):
        self.now = now()
        self.now_earlier = self.now + datetime.timedelta(hours=-24)
        self.now_later = self.now + datetime.timedelta(hours=24)
        self.ct = ContentType.objects.get(app_label='time_wizard',
                                          model='timewizardmodel')

    def test_absolute_period_model(self):
        time_wizard = TimeWizardModel.objects.create()
        absolute_period = AbsolutePeriodModel.objects.create(
            content_type=self.ct,
            object_id=time_wizard.id,
        )
        self.assertTrue(absolute_period.contains(self.now))
        absolute_period.start = self.now_later
        self.assertFalse(absolute_period.contains(self.now))
        absolute_period.start = self.now_earlier
        self.assertTrue(absolute_period.contains(self.now))
        absolute_period.end = self.now_earlier
        self.assertFalse(absolute_period.contains(self.now))

    def test_holiday_range_period_model_time(self):
        time_wizard = TimeWizardModel.objects.create()
        holiday_date, holiday = holidays.US(years=self.now.year).popitem()
        holiday_date = datetime.datetime.combine(holiday_date, self.now.time())
        holiday_range = HolidayRangePeriodModel.objects.create(
            content_type=self.ct,
            object_id=time_wizard.id,
            country='US',
            holiday=holiday,
        )
        holiday_date_earlier = holiday_date + datetime.timedelta(days=-1)
        holiday_date_later = holiday_date + datetime.timedelta(days=1)
        self.assertTrue(holiday_range.contains(holiday_date))
        self.assertFalse(holiday_range.contains(holiday_date_earlier))
        self.assertFalse(holiday_range.contains(holiday_date_later))
        holiday_time_earlier = (holiday_date +
                                datetime.timedelta(hours=-1)).time()
        holiday_time_later = (holiday_date +
                              datetime.timedelta(hours=1)).time()
        holiday_range.start_time = holiday_time_later
        self.assertFalse(holiday_range.contains(holiday_date))
        holiday_range.start_time = holiday_time_earlier
        self.assertTrue(holiday_range.contains(holiday_date))
        holiday_range.end_time = holiday_time_later
        self.assertTrue(holiday_range.contains(holiday_date))
        holiday_range.end_time = self.now.time()
        self.assertFalse(holiday_range.contains(now()))

    def test_holiday_range_period_model_range(self):
        time_wizard = TimeWizardModel.objects.create()
        holiday_date, holiday = holidays.US(years=self.now.year).popitem()
        holiday_date = datetime.datetime.combine(holiday_date, self.now.time())
        holiday_range = HolidayRangePeriodModel.objects.create(
            content_type=self.ct,
            object_id=time_wizard.id,
            country='US',
            holiday=holiday,
            time_value=4,
            time_unit='10080',
            range_position='before',
        )
        holiday_date_earlier = holiday_date + datetime.timedelta(weeks=-3)
        holiday_date_later = holiday_date + datetime.timedelta(weeks=1)
        self.assertTrue(holiday_range.contains(holiday_date))
        self.assertTrue(holiday_range.contains(holiday_date_earlier))
        self.assertFalse(holiday_range.contains(holiday_date_later))
        holiday_range.time_value = 2
        self.assertFalse(holiday_range.contains(holiday_date_earlier))
        holiday_range.range_position = 'both'
        self.assertTrue(holiday_range.contains(holiday_date_later))

    def test_time_wizard_is_published(self):
        time_wizard = TimeWizardModel.objects.create()
        self.assertFalse(time_wizard.is_published)
        absolute_period = AbsolutePeriodModel.objects.create(
            content_type=self.ct,
            object_id=time_wizard.id,
            start=self.now_earlier,
        )
        self.assertTrue(time_wizard.is_published)
        absolute_period.end = self.now_earlier
        absolute_period.save()
        self.assertFalse(time_wizard.is_published)

    def test_time_wizard_str(self):
        time_wizard = TimeWizardModel.objects.create()
        absolute_period_1 = AbsolutePeriodModel.objects.create(
            content_type=self.ct,
            object_id=time_wizard.id,
            start=self.now_earlier,
        )
        self.assertEqual('1 - ' + str(absolute_period_1), str(time_wizard))
        absolute_period_2 = AbsolutePeriodModel.objects.create(
            content_type=self.ct,
            object_id=time_wizard.id,
            start=self.now_earlier,
        )
        self.assertEqual('1 - {} - {}'.format(str(absolute_period_1),
                                              str(absolute_period_2)),
                         str(time_wizard))
        time_wizard.name = 'Test time wizard'
        self.assertEqual('1 - ' + time_wizard.name, str(time_wizard))
