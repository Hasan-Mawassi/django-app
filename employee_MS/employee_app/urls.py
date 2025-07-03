from django.urls import path
from .views import EmployeeListCreateView , DepartmentCreateView

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('departments/', DepartmentCreateView.as_view(), name='department-create'),
]
