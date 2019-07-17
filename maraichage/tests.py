from django.test import TestCase
from django.urls import reverse


from .models import *

class Maraichage(TestCase):

    def setUp(self):
        self.pascal = ""


    def test_dashboard_not_authenticates_user(self):
        url = reverse('maraichage:dashboard')
        response = self.client.get(url)
        self.assertTemplateNotUsed(response, 'maraichage/dashboard.html')
        self.failUnlessEqual(response.status_code, 302)


    def test_authenticates_user(self):
        self.client.login(username='pascal', password='pascal')
        response = self.client.get(reverse('maraichage:dashboard'))
        self.assertEqual(type(response.context['backlogs']))
        self.assertEqual(len(response.context['backlogs']), 2)
        self.assertEqual(type(response.context['teams']))
        self.assertEqual(len(response.context['teams']), 2)
        self.failUnlessEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'maraichage/dashboard.html')
        self.client.logout()