from rest_framework import serializers

from measurement.models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = [ 'id', 'name', 'description'] #


class MeasurementSerializer(serializers.ModelSerializer):
    #sensors = SensorSerializer(read_only=False, many=False)#Sensor.objects.id.all())#(data= 'id') #read_only=False, many=False)

    class Meta:
        model = Measurement
        fields = ['id', 'temperature', 'created_at', 'sensor']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']