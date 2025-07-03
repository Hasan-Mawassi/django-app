from rest_framework import serializers
from .models import Employee, Department, WorkSchedule

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}  
        }

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Department
        fields = '__all__'

class WorkScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model =  WorkSchedule
        fields = '__all__'
