from django.urls import path
from children import views
from newborn.views import fetch_county_municipalities, fetch_subcounties, fetch_parishes, fetch_villages

urlpatterns = [
                path('child_registration/', views.child_registration, name='child-registration-form'),
                path('child_information/<int:child_id>/', views.child_information, name='child_information'),
                path('record-measurements/<int:registration_id>/', views.record_measurements, name='record_measurements'),
                path('children_lab_request/<int:child_id>/', views.children_lab_request, name='children_lab_request'),
                path('pending-tests/<int:child_id>/', views.pending_tests_for_child, name='pending-tests-for-child'),
                path('fetch-county-municipalities/<int:district_id>/', fetch_county_municipalities, name='fetch_county_municipalities'),
                path('fetch-subcounties/<int:county_municipality_id>/', fetch_subcounties, name='fetch_subcounties'),
                path('fetch-parishes/<int:subcounty_id>/', fetch_parishes, name='fetch_parishes'),
                path('fetch-villages/<int:parish_id>/', fetch_villages, name='fetch_villages'),
            ]
