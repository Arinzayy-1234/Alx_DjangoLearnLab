
from django.urls import path
from .import views
from .views import list_books, LibraryDetailView, SignupView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('books/', list_books, name = 'all_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(),name = 'library_detail'),
    # Add other URL patterns here as needed
    path('account/signup/', SignupView.as_view(), name = 'register'),
    path('account/login/', LoginView.as_view(template_name='relationship_app/login.html'), name = 'login'),
    path('account/logout/', LogoutView.as_view(template_name = 'relationship_app/logout.html'), name = 'logout'),
]