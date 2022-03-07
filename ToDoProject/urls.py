from django.contrib import admin
from django.urls import path
from ToDoApp import views
urlpatterns = [
    path('', views.saveinfo, name='saveinfo'),
    path('saveinfo/', views.saveinfo, name='saveinfo'),
    path('index/', views.index, name='index'),
    path('Delete/<int:id>',views.Delete,name='Delete'),
    path('about/',views.about),
]