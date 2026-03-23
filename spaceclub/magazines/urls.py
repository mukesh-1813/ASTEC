from django.urls import path
from . import views

app_name = 'magazines'

urlpatterns = [
    path('', views.magazine_list, name='list'),
    path('<int:pk>/', views.magazine_detail, name='detail'),
]
