from rest_framework import generics
from ..models import Employee
from ..serializers import EmployeeSerializer
from ..permissions import IsHR
from rest_framework.permissions import IsAuthenticated


class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated, IsHR]