from rest_framework import permissions


class WholeWorld(permissions.BasePermission):
    """
    Object-level permission to only allow the connected user to view it.
    """

    def has_permission(self, request, view):
        return True
