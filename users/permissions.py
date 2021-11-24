from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """Админское разрешение."""
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_admin:
            return True
        return False
