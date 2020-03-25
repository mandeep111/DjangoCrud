from django.shortcuts import render, redirect
from .models import Book
from .forms import CreateBook
from django.http import HttpResponse
from django.core.paginator import Paginator

def index(request):
    shelf = Book.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(shelf,5)
    page_obj = paginator.get_page(page_number)
   
    return render(request, 'book/library.html', {'shelf': page_obj})

def detail(request, book_id):
    shelf = Book.objects.get(id = book_id)
    print(shelf)
    return render(request, 'book/detail.html', {'shelf': shelf})