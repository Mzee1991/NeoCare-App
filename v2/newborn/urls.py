from django.urls import path
from newborn import views

urlpatterns = [
    path('newborn/', views.newborn_list),
    path('newborn/<int:pk>/', views.newborn_detail),
    path('newborn/index/', views.index, name='add-newborn'),
    path('newborn/print/<int:pk>/', views.print_detail),
    path('newborn/print_care2x/', views.print_care2x),
    path('newborn/clerkship/', views.print_clerkship),
    path('newborn/mother/', views.mother, name='mother-details'),
   #path('', views.home, name='newborn-home'),
    path('', views.newborn_table, name='home-page'),
    path('newborn/search/', views.newborn_search, name='search-newborn'),
]
