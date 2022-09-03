from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsOwnerOrReadOnly]
    throttle_classes = [AnonRateThrottle]
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ['creator', 'created_at',]
    def get_permissions(self) -> object:
         """Получение прав для действий."""
         if self.action in ["create", "update", "partial_update"]:
             return [IsAuthenticated()]
         return []


