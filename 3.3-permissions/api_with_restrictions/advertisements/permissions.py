from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

from advertisements.models import Advertisement


class IsOwnerOrReadOnly(permissions.BasePermission):

    def get_permissions(self) -> object:
         """Получение прав для действий."""
         if self.action in ["create", "update", "partial_update"]:
             return [IsAuthenticated()]
         return []

    def has_permission(self, request, view):
         if request.method == 'GET':
             return True
         if request.method == 'POST' \
                 and Advertisement.objects.filter(creator=request.user, status = 'OPEN').count() < 10:# Фильтрация созданных  - не более 10
             return [IsAuthenticated()]
         return []

    # def has_object_permission(self, request, view, obj):
    #     print(obj.creator)  # admin Token 8affcdadbdd6b9f8ebefa5a552aa127ebff60178
    #     print('Check IT!!!!!')
    #     print(request.user)
    #     if request.method == 'PATCH':
    #         return request.user.is_authenticated and obj.creator == request.user
    #     return []



# class IsAuthenticatedAndOwner(BasePermission):
#     message = 'You must be the owner of this object.'
#     def has_permission(self, request, view):
#         return request.user and request.user.is_authenticated
#     def has_object_permission(self, request, view, obj):
#         return obj.user == request.user
