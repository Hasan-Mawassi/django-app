from rest_framework import serializers
from .models import Employee, Department, WorkSchedule , HR
from django.contrib.auth.models import User


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


class HRRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    department = serializers.CharField()
    hire_date = serializers.DateField()

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        department = validated_data["department"]
        hire_date = validated_data["hire_date"]

        # Create User
        user = User.objects.create_user(username=username, password=password)

        # Create HR profile
        HR.objects.create(user=user, department=department, hire_date=hire_date)

        return user
