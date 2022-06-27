from django.db import models

class Sensor(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=256, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    #chains

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
        ordering = ['-id']

    def __str__(self):
        return self.id

class Measurement (models.Model):
    temperature = models.FloatField(verbose_name='Температура при измерении')
    created_at = models.DateTimeField(verbose_name='Дата замера')
    sensor = models.ManyToManyField(Sensor, through='Chain', related_name= 'measurements')
#    class DateField(auto_now=False, auto_now_add=False, **options)???
 #   image = models.ImageField(null=True, blank=True, verbose_name='Изображение замера')
    # chains
    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
        ordering = ['-created_at']
    def __str__(self):
        return self.created_at


class Chain (models.Model):
    id_sensor = models.PositiveIntegerField( default = 999, verbose_name='ID датчика')
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name= 'chains')
    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE, related_name='chains')

    class Meta:
        verbose_name = 'иЗМЕРЕНИЕ датчика'
        verbose_name_plural = 'иЗМЕРЕНИЯ датчика'
