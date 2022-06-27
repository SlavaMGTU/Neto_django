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

    def post(self, request):#, new_id, name, description):
        # ordering = '-id'
        # date = {}
        # date = {'object_list': Sensor.objects.all().order_by(ordering)}#
        # new_id=1
        # while new_id in date['object_list']:
        #     new_id += 1
        #Sensor(id=new_id, name =name, description=description).save()
        return Response({'status': 'OK'}) #f'new sensor: id='{new_id})#
    # r = request.post(url=url, headers=headers, data=data)


class SensorDetailView(RetrieveAPIView):#RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer