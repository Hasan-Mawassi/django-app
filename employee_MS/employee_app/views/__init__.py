from .department_views import DepartmentCreateView , DepartmentDeleteView , DepartmentUpdateView
from .employee_views import EmployeeListView
from .hr_views import HRRegisterView , HRLoginView
__all__ = [
    'EmployeeListView', 
    'DepartmentCreateView', 
    'DepartmentDeleteView', 
    'DepartmentUpdateView',
    'HRRegisterView',
    'HRLoginView'
    ]