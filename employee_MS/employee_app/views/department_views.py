from rest_framework import generics
from ..models import Department
from ..serializers import DepartmentSerializer
from ..permissions import IsHR
from rest_framework.permissions import IsAuthenticated

class DepartmentCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated, IsHR]

class DepartmentDeleteView(generics.DestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer  
    permission_classes = [IsAuthenticated, IsHR]
    
class DepartmentUpdateView(generics.UpdateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated, IsHR]