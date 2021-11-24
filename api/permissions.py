from rest_framework.permissions import (BasePermission,
                                        IsAuthenticatedOrReadOnly)


class AuthorStaffOrReadOnly(IsAuthenticatedOrReadOnly):

    def has_object_permission(self, request, view, obj):
        return (
            request.method in 'GET'
            or request.user.is_moderator or request.user.is_admin
            or request.user == obj.author
        )


class AdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return (
            request.method in 'GET'
            or request.user.is_authenticated
            and request.user.is_admin
        )
