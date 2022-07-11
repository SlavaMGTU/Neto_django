from django.contrib import admin

from logistic.models import Product, Stock


@admin.register(Product)
class ArticleAdmin(admin.ModelAdmin):
    #list_display = ['id','Scope']
    pass

@admin.register(Stock)
class ScopeAdmin(admin.ModelAdmin):
    pass
