import holidays
from django.test import RequestFactory, TestCase
from django.utils.timezone import now
from django.urls import reverse

from time_wizard.views import load_holidays


class TestTimeWizardModel(TestCase):
    def setUp(self):
        self.rf = RequestFactory()

    def test_load_holidays(self):
        request = self.rf.get('/test/', {'country': 'US', 'province': 'AL'})
        response = load_holidays(request)
        holiday_cls = getattr(holidays, 'US')
        holidays_list = holiday_cls(years=now().year, prov='AL')
        content = response.content.decode("utf-8")
        content = content.replace('&#x27;', "'").replace('&amp;', '&')
        self.assertIn('<option value="">---------</option>', content)
        for date, name in holidays_list.items():
            html = '<option value="{0}">{0} ('.format(name)
            self.assertIn(html, content)

    def test_urls_definition(self):
        urlconf = "time_wizard.urls"
        cases = [
            ("/load-holidays", "ajax-load-holidays"),
        ]
        for expected_path, url_name in cases:
            with self.subTest(url_name):
                actual_path = reverse(url_name, urlconf=urlconf)
                self.assertEqual(expected_path, actual_path)
