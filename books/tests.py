from django.test import TestCase
from django.urls import reverse, resolve
from .views import book_detail_view, BookListView

class BookTest(TestCase):
    def test_book_list_view_by_url(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)

    def test_book_list_view_by_name(self):
        response = self.client.get(reverse('books:book_list'))
        self.assertEqual(response.status_code, 200)

    def test_book_list_use_template(self):
        response = self.client.get(reverse('books:book_list'))
        self.assertTemplateUsed(response, 'books/book_list.html')
    
    def test_use_correct_book_list_view_in_url_by_name(self):
        url = reverse('books:book_list')
        self.assertEqual(resolve(url).func.view_class,BookListView )

    def test_use_correct_view_in_url_book_detail(self):
        url = reverse('books:book_detail', args=[1])
        self.assertEqual(resolve(url).func,book_detail_view )
