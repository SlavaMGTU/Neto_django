from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

from advertisements.models import Advertisement


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        if request.method == 'PATCH':
            return obj.creator == request.user #request.user.is_authenticated and
        return []
