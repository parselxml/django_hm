import json

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from books.models import Book


def create_books(request):
    with open('dj-homeworks/2.1-databases/models_list_displaying/fixtures/books.json', 'r', encoding='utf-8') as f:
        books_data = json.load(f)

    created_books = []

    for book in books_data:
        fields = book['fields']
        new_book = Book(name=fields['name'], author=fields['author'], pub_date=fields['pub_date'])
        new_book.save()
        created_books.append(new_book.name)
    return HttpResponse(f"Создано {len(created_books)} книг: {', '.join(created_books)}.")


def books_view(request, pub_date=None):
    template = 'books/books_list.html'

    if pub_date:
        books = Book.objects.filter(pub_date=pub_date)
    else:
        books = Book.objects.all()

    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    if pub_date:
        previous_date = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').first()
        next_date = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()
    else:
        previous_date = None
        next_date = None

    context = {
        'page': page,
        'books': books,
        'previous_date': previous_date.pub_date if previous_date else None,
        'next_date': next_date.pub_date if next_date else None,
    }

    return render(request, template, context)