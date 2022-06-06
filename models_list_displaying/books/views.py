from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, template, context)

def books_by_date(request, dt):
    template = 'books/books_list.html'

    all_dates = [book['pub_date'] for book in Book.objects.order_by('pub_date').values('pub_date').distinct()]

    paginator = Paginator(all_dates, 1)
    index = all_dates.index(dt)
    page = paginator.get_page(index+1)
    print(all_dates, index)
    print(page.has_next(), page.has_previous())

    if page.has_next():
        next_date = all_dates[index+1]
    else:
        next_date = None
    
    if page.has_previous():
        previous_date = all_dates[index-1]
    else:
        previous_date = None

    books = Book.objects.filter(pub_date=dt)
    context = {
        'next_date': next_date,
        'previous_date': previous_date,
        'page': page,
        'books': books
    }

    return render(request, template, context)