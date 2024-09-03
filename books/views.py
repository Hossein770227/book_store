from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Book, Comment
from .forms import CommentForm

class BookListView(ListView):
    model =Book
    template_name= 'books/book_list.html'
    context_object_name = 'books'

    ordering = ['-date_time_created']



def book_detail_view(request, pk):
    book = get_object_or_404(Book,pk=pk )
    comment =Comment.objects.filter(active=True)
    if request.method =='POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.book = book
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    return render(request,'books/book_detail.html',{'book':book,"comments":comment, 'comment_form': comment_form} )