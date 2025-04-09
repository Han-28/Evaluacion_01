from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_manga, name='search_manga'),
    path('list/', views.manga_list, name='manga_list'),
    path('save/', views.save_manga, name='save_manga'),
    path('manga/<int:pk>/', views.manga_detail, name='manga_detail'),
    path('edit/<int:pk>/', views.edit_manga, name='edit_manga'),
    path('delete/<int:pk>/', views.delete_manga, name='manga_delete'),

]