from django.test import TestCase
from django.shortcuts import reverse

class LandingPageTest(TestCase):
  def test_status_code(self):
    response = self.client.get(reverse('landing_page'))
    self.assertEqual(response.status_code, 200)