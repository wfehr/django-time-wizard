import holidays
from django.test import RequestFactory, TestCase
from django.utils.timezone import now
from django.urls import reverse

from time_wizard.conf import TIME_WIZARD_COUNTRY_PROVINCES
from time_wizard.views import load_holidays, load_provinces


class TestTimeWizardModel(TestCase):
    def setUp(self):
        self.rf = RequestFactory()

    def test_load_holidays(self):
        request = self.rf.get('/test/', {'country': 'US', 'province': 'AL'})
        response = load_holidays(request)
        holiday_cls = getattr(holidays, 'US')
        holidays_list = holiday_cls(years=now().year, prov='AL')
        content = response.content.decode("utf-8").replace('&#x27;', "'")
        self.assertIn('<option value="">---------</option>', content)
        for date, name in holidays_list.items():
            html = '<option value="{0}">{0} ('.format(name)
            self.assertIn(html, content)

    def test_load_provinces(self):
        request = self.rf.get('/test/', {'country': 'US'})
        response = load_provinces(request)
        content = response.content.decode("utf-8").replace('&#x27;', "'")
        self.assertIn('<option value="">---------</option>', content)
        for province in TIME_WIZARD_COUNTRY_PROVINCES['US']:
            html = '<option value="{0}">{0}</option>'.format(province)
            self.assertIn(html, content)

    def test_urls_definition(self):
        urlconf = "time_wizard.urls"
        cases = [
            ("/load-holidays", "ajax-load-holidays"),
            ("/load-provinces", "ajax-load-provinces"),
        ]
        for expected_path, url_name in cases:
            with self.subTest(url_name):
                actual_path = reverse(url_name, urlconf=urlconf)
                self.assertEqual(expected_path, actual_path)
