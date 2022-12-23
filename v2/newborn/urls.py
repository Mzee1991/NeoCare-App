from django.urls import path
from newborn import views

urlpatterns = [
    path('newborn/', views.newborn_list),
    path('newborn/<int:pk>/', views.newborn_detail),
    path('newborn/index/', views.index, name='add-newborn'),
    path('newborn/print/', views.print_detail),
    path('newborn/mother/', views.mother, name='mother-details'),
   #path('', views.home, name='newborn-home'),
    path('', views.newborn_table, name='home-page'),
    path('newborn/search/', views.newborn_search, name='search-newborn'),
]
