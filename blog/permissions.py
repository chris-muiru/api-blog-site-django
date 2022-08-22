from rest_framework import permissions


class isWritterOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_writter == True:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_writter:
            return True
        return False
