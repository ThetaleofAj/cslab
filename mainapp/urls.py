from django.urls import path
from .views import ListView,CreateView
from django.conf.urls import url
from . import views

urlpatterns = [
   path('home',ListView.as_view()),
   path('post',CreateView.as_view()),

]