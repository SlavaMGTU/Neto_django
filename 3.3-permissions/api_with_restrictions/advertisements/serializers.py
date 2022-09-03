from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию. Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя. обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.  само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""

        # TODO: добавьте требуемую валидацию
        if self.context["request"].method == 'PATCH'\
                       and Advertisement.objects.filter(creator=self.context["request"].user, status = 'OPEN').count() < 10: #Фильтрация созданных  - не более 10
                   return True
        else:
            message = 'You must CLOSE some advartisments.'
        return data



        # def has_object_permission(self, request, view, obj):
        #     print(obj.creator)  # admin Token 8affcdadbdd6b9f8ebefa5a552aa127ebff60178
        #     print('Check IT!!!!!')
        #     print(request.user)
        #     if request.method == 'PATCH':
        #         return request.user.is_authenticated and obj.creator == request.user
        #     return []

