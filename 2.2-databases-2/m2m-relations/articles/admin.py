from .models import Article, Tag, Scope
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class TagInlineFormset(BaseInlineFormSet):
    def clean(self):
        a=0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if form.cleaned_data['is_main']== True:
                a=+1
                # form.cleaned_data #= {'scope': Scope.objects.all()}
                # вызовом исключения ValidationError можно указать админке о наличие ошибки
                # таким образом объект не будет сохранен,
                # а пользователю выведется соответствующее сообщение об ошибке
            if a>1:
                raise ValidationError('Тут всегда ошибка')
        return super().clean()  # вызываем базовый код переопределяемого метода

class TagInline(admin.TabularInline):
    model = Tag
    formset = TagInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    #list_display = ['id','Scope']

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass



