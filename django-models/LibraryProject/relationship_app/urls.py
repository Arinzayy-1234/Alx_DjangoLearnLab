
from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.AllBooks, name = 'all_books'),
    path('library/<int:pk>/', views.LibraryView.as_view(),name = 'library_detail'),
    # Add other URL patterns here as needed
]