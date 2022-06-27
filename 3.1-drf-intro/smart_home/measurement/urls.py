from django.contrib import admin
from django.urls import path
from measurement.views import SensorsView, SensorDetailView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsView.as_view()),
    path('sensor/<pk>', SensorDetailView.as_view()),
    path('sensors/<id>/<name>/<description>', SensorsView.as_view()),
]
