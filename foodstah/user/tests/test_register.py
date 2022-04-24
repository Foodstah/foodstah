#!/usr/bin/env python3

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class ModelBaseTest(TestCase):
    def setUp(self):
        self.user = {
            "username": "Daniel",
            "email": "test@test.com",
            "password": "password",
        }
    def tearDown(self):
        self.user.delete()


class SignUpModelTest(ModelBaseTest):
    def test_signup_page(self):
        response = self.client.get("/signup/")
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            "/signup/",
            {
                "username": "Tester_McTestsalot",
                "email": "email@email.com",
                "password1": "password",
                "password2": "password",
            },
        )
        self.assertEqual(response.status_code, 200)

    def test_user_registration(self):
        user = get_user_model().objects.create_user(**(self.user))
        self.assertEquals(user.username, self.user["username"])
        self.assertEquals(user.email, self.user["email"])
        self.assertTrue(user.check_password(self.user["password"]))
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)


    def test_user_profile_created_on_registration(self):
        user = get_user_model().objects.create_user(**(self.user))
        username = user.username
        self.client.login(username="Daniel", password="password")
        response = self.client.get(f"/profile/{username}/")
        self.assertContains(response, f"{username}")
        self.assertEqual(response.status_code, 200)
