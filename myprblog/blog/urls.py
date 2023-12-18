from django.urls import path
from .views import post_list, post_detail,home

urlpatterns = [
    path('home/', home, name='home'),
    path('post_list/', post_list, name='post_list'),
    path('post_detail/<int:pk>/', post_detail, name='post_detail'),
]