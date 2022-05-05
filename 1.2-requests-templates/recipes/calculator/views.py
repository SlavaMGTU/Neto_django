from django.http import HttpResponse
from django.shortcuts import render
#from django.urls import reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
     },
    'pasta': {
         'макароны, кг': 0.3,
         'сыр, кг': 0.05,
     },
    'buter': {
         'хлеб, ломтик': 1,
         'колбаса, ломтик': 1,
         'сыр, ломтик': 1,
         'помидор, ломтик': 1,
     },
    'hot-dog': {
        'сосиска, шт': 1,
         'булочка, шт': 1,
         'кетчуп, гр': 2,
         'горчица, гр': 1,
     },
    # можете добавить свои рецепты ;)
}
#{% empty %}# index.html
#    <p>Такого рецепта не знаю :(</p>


def view(request, dish):
    context = {
        'recipe': {},
    }
    amount = int(request.GET.get("servings", 1))
    #if dish in DATA:
    for key, value in DATA[dish].items():
        DATA[dish][key] = value * amount
    context['recipe'] = DATA[dish]
    return render(request, 'calculator/index.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
#/omlet/?servings=4
#/hot-dog/?servings=2
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
