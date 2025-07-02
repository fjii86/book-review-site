from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('signup/', views.signup, name='signup'),
]