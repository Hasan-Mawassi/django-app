from .department_views import DepartmentCreateView , DepartmentDeleteView , DepartmentUpdateView
from .employee_views import EmployeeListCreateView
from .hr_views import HRRegisterView , HRLoginView
__all__ = [
    'EmployeeListCreateView', 
    'DepartmentCreateView', 
    'DepartmentDeleteView', 
    'DepartmentUpdateView',
    'HRRegisterView',
    'HRLoginView'
    ]