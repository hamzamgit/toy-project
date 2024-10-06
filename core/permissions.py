from rest_framework import permissions


class HasEditorPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        if user.is_editor_by_permission:
            return True
