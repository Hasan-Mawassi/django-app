from django.urls import path
from .views import EmployeeListCreateView , DepartmentCreateView , DepartmentDeleteView 

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('departments/', DepartmentCreateView.as_view(), name='department-create'), 
    path('departments/<int:pk>/', DepartmentDeleteView.as_view(), name='department-delete'),
    path('departments/<int:pk>/', DepartmentDeleteView.as_view(), name='department-delete'),
]
