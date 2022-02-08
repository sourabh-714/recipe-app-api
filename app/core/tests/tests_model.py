from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """test creating a new user with an email is successful"""
        email="test@ncuindia.edu"
        password="Testpass123"
        user=get_user_model().objects.create_user(email=email,password=password)
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
    
    
    def test_new_user_email_normalized(self):
        """test the email for new use ris normalized """
        email=test@NCUINDIA.EDU
        user=get_user_model().objects.create_userf(email=email,test@123)
        self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):
        """test creating user with no email raises error"""
        with self.assertRaises(Value_Error):
            get_user_model_().objects.create_user(None,'test@123')

    