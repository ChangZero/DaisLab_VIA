from django.urls import path
from . import views

urlpatterns = [
    path('via/', views.viaindex, name='via-index'),
    path('upload/', views.postupload, name='myapp-upload'),
    path('index/', views.index, name='myapp-index'),
    path('index/detail/<int:post_id>/', views.detail, name='myapp-detail'),
    path('index/delete/<int:post_id>/',
         views.delete, name='myapp-delete'),
    path('index/edit/<int:post_id>/', views.edit, name='myapp-edit'),
]
