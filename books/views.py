from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Book, Comment

class BookListView(ListView):
    model =Book
    template_name= 'books/book_list.html'
    context_object_name = 'books'


# class BookDetailView(DetailView):
#     model =Book
#     template_name = 'books/book_detail.html'
#     context_object_name = 'book'

def book_detail_view(request, pk):
    book = get_object_or_404(Book,pk=pk )
    comment =Comment.objects.filter(active=True)
    return render(request,'books/book_detail.html',{'book':book,"comments":comment} )