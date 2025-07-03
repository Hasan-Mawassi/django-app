from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255) 
    password = models.CharField(max_length=255) 
    position = models.CharField(max_length=200) 
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="employees"
    )
    hire_date = models.DateField()