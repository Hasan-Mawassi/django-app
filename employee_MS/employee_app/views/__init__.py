from .department_views import DepartmentCreateView , DepartmentDeleteView , DepartmentUpdateView
from .employee_views import EmployeeListView , EmployeeCreateView , EmployeeUpdateView
from .hr_views import HRRegisterView , HRLoginView
__all__ = [
    'EmployeeListView', 
    'EmployeeCreateView',
    'EmployeeUpdateView',
    'DepartmentCreateView', 
    'DepartmentDeleteView', 
    'DepartmentUpdateView',
    'HRRegisterView',
    'HRLoginView'
    ]