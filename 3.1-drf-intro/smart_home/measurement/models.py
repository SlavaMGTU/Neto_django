from django.db import models

class Sensor(models.Model):
    #id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=256, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    #chains

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
        ordering = ['id']

    def __str__(self):
        return self.id

class Measurement(models.Model):
    temperature = models.FloatField(verbose_name='Температура при измерении')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата замера')
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name= 'measurements')#ManyToManyField through='Chain',
#    class DateField(auto_now=False, auto_now_add=False, **options)???
 #   image = models.ImageField(null=True, blank=True, verbose_name='Изображение замера')
    # chains
    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
        ordering = ['-created_at']
    def __str__(self):
        return self.created_at


# class Chain (models.Model):
#     sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name= 'chains')
#     measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE, related_name='chains')
#
#     class Meta:
#         verbose_name = 'иЗМЕРЕНИЕ датчика'
#         verbose_name_plural = 'иЗМЕРЕНИЯ датчика'
