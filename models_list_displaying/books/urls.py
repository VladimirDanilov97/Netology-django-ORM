from django.urls import path
from .views import books_view, books_by_date
from django.urls import register_converter
from .converters import PubDateConverter

register_converter(PubDateConverter, 'date')

urlpatterns = [
    path('books/', books_view, name='books'),
    path('books/<date:dt>/', books_by_date, name='books_by_date')
]