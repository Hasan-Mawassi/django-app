from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path('employees/', views.EmployeeListView.as_view(), name='employee-list'),
    path('employee/create/', views.EmployeeCreateView.as_view(), name='employee-create'),
    path('employee/<int:id>/update/', views.EmployeeUpdateView.as_view(), name='employee-update'),
    path('employee/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee-delete'),
    path('departments/', views.DepartmentCreateView.as_view(), name='department-create'), 
    path('department/<int:pk>/delete/', views.DepartmentDeleteView.as_view(), name='department-delete'),
    path('department/<int:pk>/update/', views.DepartmentUpdateView.as_view(), name='department-update'),
    path('hr-login/', views.HRLoginView.as_view(), name='hr-login'),
    path('hr-register/', views.HRRegisterView.as_view(), name='hr-register'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
