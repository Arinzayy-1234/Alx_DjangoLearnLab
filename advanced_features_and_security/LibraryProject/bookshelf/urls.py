
from django.urls import path
from .  import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/add/', views.book_create, name='book_create'),
    path('books/<int:pk>/edit/', views.book_edit, name= 'book_edit'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('example-form/', views.example_form_view, name='example_form'),
]