from django.urls import path 
from book import views 

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('book/create/',views.BookCreateView.as_view(),name='book-create'),
    path('books/',views.BookListView.as_view(),name='book-list'),
    path('books/<int:pk>/',views.BookDetailView.as_view(),name='book-detail'),
    path('books/<int:pk>/edit/', views.BookUpdateView.as_view(), name='book-edit'),
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),
    ]
