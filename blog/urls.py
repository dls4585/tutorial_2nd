from django.urls import path
from . import views

urlpatterns = [
    #127.0.0.1:8000/ 으로 들어오면 view.post_list를 보여줘
    #기본화면
    path('', views.post_list, name='post_list'),
]