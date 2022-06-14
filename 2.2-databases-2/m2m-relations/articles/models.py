from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    #scopes
    #tag

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

class Scope (models.Model):
    name = models.CharField(max_length=30, verbose_name='Раздел')
    article = models.ManyToManyField(Article, through='Tag', related_name= 'scopes')
    # tag

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

class Tag (models.Model):
    is_main = models.BooleanField(default=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name= 'tag')
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE, related_name= 'tag')