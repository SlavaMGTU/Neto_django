from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from measurement.models import Sensor
from measurement.serializers import SensorSerializer, SensorDetailSerializer


# class sensorsView(ListCreateAPIView):
#     def get(self, request):
#         sensors = Sensor.objects.all()
#         ser = SensorSerializer(sensors, many=True)
#         return Response(ser.data)
#
#     def post(self, request):
#         return Response({'status': 'OK'})


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        input()
        #r = request.post(url=url, headers=headers, data=data)
        return Response({'status': 'OK'})


class SensorDetailView(RetrieveAPIView):#RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer