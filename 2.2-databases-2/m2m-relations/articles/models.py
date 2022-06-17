from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    #scopes
    #tags

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

class Scope (models.Model):
    name = models.CharField(max_length=30, verbose_name='Тематика')
    article = models.ManyToManyField(Article, through='Tag', related_name= 'scopes')
    # tags
    class Meta:
        verbose_name = 'РАЗДЕЛЫ'
        verbose_name_plural = 'РАЗДЕЛЫ'

    def __str__(self):
        return self.name

class Tag (models.Model):
    is_main = models.BooleanField(default=True, verbose_name='ОСНОВНОЙ')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name= 'tags')
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE, related_name= 'tags', verbose_name='РАЗДЕЛ')

    class Meta:
        verbose_name = 'ТЕМАТИКА'
        verbose_name_plural = 'ТЕМАТИКИ СТАТЬИ'