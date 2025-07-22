
from django.urls import path
from .import views
from .views import list_books, LibraryDetailView


urlpatterns = [
    path('books/', views.list_books, name = 'all_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(),name = 'library_detail'),
    # Add other URL patterns here as needed
]