from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer

class IsOwnerOrReadOnly(permissions.BasePermission):
    # """
    # Object-level permission to only allow owners of an object to edit it.
    # Assumes the model instance has an `owner` attribute.
    # """
    #
    # def has_object_permission(self, request, view, obj):
    #     # Read permissions are allowed to any request,
    #     # so we'll always allow GET, HEAD or OPTIONS requests.
    #     if request.method in permissions.SAFE_METHODS:
    #         return True
    #
    #     # Instance must have an attribute named `owner`.
    #     return obj.owner == request.user
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return request.user.is_authenticated and obj.author == request.user



class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsOwnerOrReadOnly]
    #throttle_classes = [AnonRateThrottle]


    def get_permissions(self) -> object:
         """Получение прав для действий."""
         if self.action in ["create", "update", "partial_update"]:
             return [IsAuthenticated()]
         return []
