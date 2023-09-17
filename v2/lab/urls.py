from django.urls import path
from lab import views


urlpatterns = [
        path('lab_requests_dashboard/', views.lab_requests_dashboard, name='lab-requests-dashboard'),
        path('lab_request/<int:pk>/', views.lab_request, name='lab-request'),
        path('lab/<int:neonate_pk>/pending_lab_tests/<int:lab_request_pk>/', views.pending_lab_tests, name='pending-lab-tests'),
        path('lab/<int:neonate_pk>/lab_request/<int:lab_request_pk>/input_lab_result/<str:test_name>/', views.input_lab_result, name='input-lab-result'),
    ]

