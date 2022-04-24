#!/usr/bin/env python3

from django.test import TestCase
from django.contrib.auth.models import User

class ModelBaseTest(TestCase):
    def setUp(self):
        self.credentials = {
            "username": "Tester_McTestsalot",
            "email": "test@test.com",
            "password": "password",
        }
        self.user = User.objects.create_user(**self.credentials)
    def tearDown(self):
        self.user.delete()

class LogInModelTest(ModelBaseTest):
    def test_login_page(self):
        response = self.client.get("/login/")
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            "/login/",
            {
                "username": "Tester_McTestsalot",
                "password1": "password",
            },
        )
        self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, "/food-feed/"))