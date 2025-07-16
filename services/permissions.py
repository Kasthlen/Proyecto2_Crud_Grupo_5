from rest_framework.permissions import BasePermission

class EsAdmin(BasePermission):
    """
    Solo usuarios con is_staff=True pueden entrar.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)


class EsEditor(BasePermission):
    """
    Solo usuarios que estén en el grupo 'Editores' pueden entrar.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and 
                    request.user.groups.filter(name='Editores').exists())
