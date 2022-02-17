from django.urls import path
from . import views
from .views import FishList, FishCreate, FishDelete


urlpatterns = [
    path('', views.FishList.as_view(), name='fish_index'),
    path('create/', views.FishCreate.as_view(), name='fish_create'),
    path('delete/<int:pk>/', views.FishDelete.as_view(), name='fish_delete'),
]
