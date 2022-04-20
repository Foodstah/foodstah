#!/usr/bin/env python3

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class ModelBaseTest(TestCase):
    def setUp(self):
        self.user = {
            "username": "Raphiie",
            "email": "test@test.com",
            "password": "se",
        }


class SignUpModelTest(ModelBaseTest):

    def test_user_registration(self):
        user = get_user_model().objects.create_user(**(self.user))
        self.assertEquals(user.username, self.user["username"])
        self.assertEquals(user.email, self.user["email"])
        self.assertTrue(user.check_password(self.user["password"]))
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)


    # def test_value_error_when_email_is_none(self):
    #     with self.assertRaises(ValueError):
    #         self.user["email"] = None
    #         get_user_model().objects.create_user(**(self.user))

    # def test_value_error_when_email_is_empty(self):
    #     with self.assertRaises(ValueError):
    #         self.user["email"] = ""
    #         get_user_model().objects.create_user(**(self.user))

    # def test_email_passes_with_standard_email_address(self):
    #     with self.assertRaises(ValueError):
    #         self.user["email"] = "test@test.com"
    #         get_user_model().objects.create_user(**(self.user))



# class RegisterSuperuserModelTest(ModelBaseTest):
#     def test_value_error_when_email_is_none(self):
#         with self.assertRaises(ValueError):
#             self.user["email"] = None
#             get_user_model().objects.create_user(**(self.user))

#     def test_value_error_when_email_is_empty(self):
#         with self.assertRaises(ValueError):
#             self.user["email"] = ""
#             get_user_model().objects.create_user(**(self.user))

#     def test_value_error_when_is_staff_false(self):
#         with self.assertRaises(ValueError):
#             get_user_model().objects.create_superuser(**(self.user), is_staff=False)

#     def test_value_error_when_is_superuser_false(self):
#         with self.assertRaises(ValueError):
#             get_user_model().objects.create_superuser(**(self.user), is_superuser=False)

#     def test_superuser_registration(self):
#         user = get_user_model().objects.create_superuser(**(self.user))
#         self.assertEquals(user.username, self.user["username"])
#         self.assertEquals(user.first_name, self.user["first_name"])
#         self.assertEquals(user.email, self.user["email"])
#         self.assertTrue(user.check_password(self.user["password"]))
#         self.assertTrue(user.is_superuser)
#         self.assertTrue(user.is_staff)
#         self.assertTrue(user.is_active)
