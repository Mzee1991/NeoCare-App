from django.urls import path
from newborn import views

urlpatterns = [
    path('newborn/', views.newborn_list),
    path('newborn/<int:pk>/', views.newborn_detail),
    path('newborn/discharge/<int:pk>/', views.discharge_form, name='discharge'),
    path('newborn/index/', views.index, name='add-newborn'),
    path('newborn/antenatal_hx/', views.antenatal_hx, name='antenatal-details'),
    path('newborn/clinical-exam/<int:pk>/', views.newborn_exam_form, name='clinical-exam'),
    #path('newborn/delivery/', views.delivery_view, name='delivery-details'),
    path('newborn/lab_request/<int:pk>/', views.lab_request, name='lab-request'),
    path('newborn/print/<int:pk>/', views.print_detail, name='clerkship-page'),
    path('newborn/dashboard', views.dashboard, name='dashboard'),
    path('newborn/print_care2x/<int:pk>', views.print_care2x, name='more-details'),
    path('newborn/clerkship/', views.print_clerkship),
    path('newborn/mother/', views.mother, name='mother-details'),
    path('newborn/birth/', views.create_birth_record, name='create-birth-record'),
   #path('', views.home, name='newborn-home'),
    path('', views.newborn_table, name='home-page'),
    path('newborn/search/', views.newborn_search, name='search-newborn'),
]
