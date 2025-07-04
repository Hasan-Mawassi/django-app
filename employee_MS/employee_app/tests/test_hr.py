from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from employee_app.models import HR
from rest_framework import status

class HRAuthTests(APITestCase):

    def setUp(self):
        # Create HR user and HR profile
        self.user = User.objects.create_user(username="hr1", password="test123")
        self.user.is_staff = True
        self.user.save()

        HR.objects.create(user=self.user, department="IT", hire_date="2023-01-01")

    def test_hr_can_login(self):
        response = self.client.post("/api/hr-login/", {
            "username": "hr1",
            "password": "test123"
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
