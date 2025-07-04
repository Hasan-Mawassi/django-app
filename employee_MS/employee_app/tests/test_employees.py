from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from employee_app.models import HR, Department, Employee
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from faker import Faker

class EmployeeFakeCreateTest(APITestCase):
    def setUp(self):
        self.faker = Faker()
        self.user = User.objects.create_user(username="hr1", password="test123", is_staff=True)
        self.hr = HR.objects.create(user=self.user, department="IT", hire_date="2023-01-01")
        self.department = Department.objects.create(name="IT")
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

    def test_create_fake_employee(self):
        fake_name = self.faker.first_name()
        fake_last_name = self.faker.last_name()
        fake_email = self.faker.email()
        fake_position = self.faker.job()
        fake_hire_date = self.faker.date()

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
        response = self.client.post("/api/employee/create/", {
            "first_name": fake_name,
            "last_name": fake_last_name,
            "email": fake_email,
            "password": "123456",
            "position": fake_position,
            "department": self.department.id,
            "hire_date": fake_hire_date
        })

        self.assertEqual(response.status_code, 201)
