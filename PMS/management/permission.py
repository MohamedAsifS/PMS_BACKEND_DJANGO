from rest_framework.permissions import DjangoModelPermissions

class PermissionForCoordinator(DjangoModelPermissions):
     perms_map = {
        'GET': ['%(management)s.add_%(PlacementRecord)s','%(management)s.add_%(Student)s','%(management)s.add_%(CompanyDepartmentYear)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(management)s.add_%(PlacementRecord)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
     
     def has_permission(self, request, view):
            if request.user.is_coordinator:
                return True 
            return False

class PermissionForStaff(DjangoModelPermissions):
     perms_map = {
        'GET': ['%(management)s.add_%(PlacementRecord)s','%(management)s.add_%(Student)s','%(management)s.add_%(CompanyDepartmentYear)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(management)s.add_%(PlacementRecord)s','%(management)s.add_%(Student)s','%(management)s.add_%(CompanyDepartmentYear)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
     
     def has_permission(self, request, view):
           
            if request.user.is_superuser:
                return True 
            return False