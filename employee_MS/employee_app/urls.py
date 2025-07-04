from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.EmployeeListView.as_view(), name='employee-list'),
    path('employees/create/', views.EmployeeCreateView.as_view(), name='employee-create'),
    path('employees/<int:id>/update/', views.EmployeeUpdateView.as_view(), name='employee-update'),
    path('departments/', views.DepartmentCreateView.as_view(), name='department-create'), 
    path('departments/<int:pk>/', views.DepartmentDeleteView.as_view(), name='department-delete'),
    path('departments/<int:pk>/update/', views.DepartmentUpdateView.as_view(), name='department-update'),
    path('hr-login/', views.HRLoginView.as_view(), name='hr-login'),
    path('hr-register/', views.HRRegisterView.as_view(), name='hr-register'),
]
