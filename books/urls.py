from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('signup/', views.signup, name='signup'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('review/new/', views.add_review, name='add_review'),
    path('add/', views.add_book, name='add_book'),
]