from django.contrib import admin
from django.urls import path
from measurement.views import SensorsView, SensorDetailView, MeasurementAddView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorDetailView.as_view()),
    path('measurements/', MeasurementAddView.as_view()),
]
