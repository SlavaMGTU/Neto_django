from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated


class IsOwnerOrReadOnly(permissions.BasePermission):

    def get_permissions(self) -> object:
         """Получение прав для действий."""
         if self.action in ["create", "update", "partial_update"]:
             return [IsAuthenticated()]
         return []

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        print(obj.author)
        print('Check IT!!!!!')
        print(request.user)
        return request.user.is_authenticated and obj.author == request.user