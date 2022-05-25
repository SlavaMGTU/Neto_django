from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    sort_by = request.GET.get('sort')
    if sort_by == 'next':
        Book.objects().
        Book.objects().filter().orders_by().first()
        # Самая маленькая из больших
    elif sort_by == 'prev':
        Book.objects().filter().orders_by().lost()# Самая большая из маленьких
    context = {'books': Book.objects.all().order_by(sort_by)}
    return render(request, template, context)

# into file books_list.html
# < div
#
#
# class ="book col-md-4" >
#
# < h2 > Сияние < / h2 >
# < p > Автор: Стивен
# Кинг < / p >
# < p > Дата
# публикации: 2018 - 0
# 9 - 10 < / p >
# < / div >
# < div
#
#
# class ="book col-md-4" >
#
# < h2 > 1984 < / h2 >
# < p > Автор: Джордж
# Оруэл < / p >
# < p > Дата
# публикации: 2015 - 03 - 11 < / p >
# < / div >
