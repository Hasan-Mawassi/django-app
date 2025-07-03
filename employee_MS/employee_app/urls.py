from django.urls import path
from .views import EmployeeListCreateView , DepartmentCreateView , DepartmentDeleteView ,DepartmentUpdateView , HRRegisterView , HRLoginView

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('departments/', DepartmentCreateView.as_view(), name='department-create'), 
    path('departments/<int:pk>/', DepartmentDeleteView.as_view(), name='department-delete'),
    path('departments/<int:pk>/update/', DepartmentUpdateView.as_view(), name='department-update'),
    path('hr-login/', HRLoginView.as_view(), name='hr-login'),
    path('hr-register/', HRRegisterView.as_view(), name='hr-register'),
]
