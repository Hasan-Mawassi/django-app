from rest_framework import generics
from ..models import Employee
from ..serializers import EmployeeSerializer
from ..permissions import IsHR
from rest_framework.permissions import IsAuthenticated


class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated, IsHR]

class EmployeeCreateView(generics.CreateAPIView):
     queryset = Employee.objects.all()
     serializer_class = EmployeeSerializer
     permission_classes = [IsAuthenticated, IsHR]

class EmployeeUpdateView(generics.UpdateAPIView):
     queryset = Employee.objects.all()
     serializer_class = EmployeeSerializer
     permission_classes = [IsAuthenticated, IsHR]
     lookup_field = 'id'

class EmployeeDeleteView(generics.DestroyAPIView):
     queryset = Employee.objects.all()
     serializer_class = EmployeeSerializer
     permission_classes = [IsAuthenticated, IsHR]
     
