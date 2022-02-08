from django.test import TestCase,Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):
    def setUp(self):
        self.client=Client()
        self.admin_user=get_user_model().objects.create_superuser(email='ncu@ncuindia.edu',
        password='pass@123')
        self.client.force_login(self.admin_user)
        self.user=get_user_model().objects.create_user(email='test@londonappdev.com',
        password='password@123',name='test user full name')

    def test_users_listed(self):
        """tests that users are listed on the user page"""
        url=reverse('admin_core_user_changelist')
        res=self.client.get(url)

        self.assertContains(res,self.user.name) 
        self.assertContains(res,self.user.email)

    def test_user_change_page(self):
        """test that user edit page works"""
        url= reverse('admin:core_user_change',args=[self.user.id])
        res=self.client.get(url)

        self.assertEqual(res.status_code, 200)
