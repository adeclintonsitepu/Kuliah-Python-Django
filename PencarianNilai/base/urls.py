from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tabel/', views.tabel, name='tabel'),
    path('read-sheet/', views.read_sheet, name='read_sheet'),
]