from django.test import TestCase
from django.urls import reverse

class HomePageViewTest(TestCase):
    def test_home_page_view_by_url(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_view_by_name(self):
        response = self.client.get(reverse('pages:home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_use_template(self):
        response = self.client.get(reverse('pages:home'))
        self.assertTemplateUsed(response, 'pages/home.html')