from django.urls import path
from newborn import views
from .views import fetch_county_municipalities, fetch_subcounties, fetch_parishes, fetch_villages

urlpatterns = [
    path('newborn/', views.newborn_list),
    path('newborn/<int:pk>/', views.newborn_detail),
    path('newborn/discharge/<int:pk>/', views.discharge_form, name='discharge'),
    path('newborn/index/', views.index, name='add-newborn'),
    path('newborn/update_details/<int:pk>/', views.update_details, name='update-details'),
    path('newborn/antenatal_hx/', views.antenatal_hx, name='antenatal-details'),
    path('newborn/mothers_antenatal_details/<int:pk>/', views.mothers_antenatal_details, name='mothers_antenatal_details'),
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
    path('fetch-county-municipalities/<int:district_id>/', fetch_county_municipalities, name='fetch_county_municipalities'),
    path('fetch-subcounties/<int:county_municipality_id>/', fetch_subcounties, name='fetch_subcounties'),
    path('fetch-parishes/<int:subcounty_id>/', fetch_parishes, name='fetch_parishes'),
    path('fetch-villages/<int:parish_id>/', fetch_villages, name='fetch_villages'),
]
