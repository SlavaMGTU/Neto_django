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
