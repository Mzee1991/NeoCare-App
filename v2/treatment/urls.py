from django.urls import path
from treatment import views

urlpatterns = [
        path('patient_treatment_chart/<int:admission_id>/', views.patient_treatment_chart, name='patient_treatment_chart'),
        path('save_prescription/', views.save_prescription, name='save_prescription'),
        path('get_prescription_details/', views.get_prescription_details, name='get_prescription_details'),
        path('get_dispensation_status/<int:dispensation_id>/', views.get_dispensation_status, name='get_dispensation_status'),
        path('get_dose1_status/<int:prescription_id>/<str:dispensation_date>/', views.get_dose1_status, name='get_dose1_status'),
        path('get_dose2_status/<int:prescription_id>/<str:dispensation_date>/', views.get_dose2_status, name='get_dose2_status'),
        path('get_dose3_status/<int:prescription_id>/<str:dispensation_date>/', views.get_dose3_status, name='get_dose3_status'),
        path('get_dose4_status/<int:prescription_id>/<str:dispensation_date>/', views.get_dose4_status, name='get_dose4_status'),
        path('dose1_status_save_dispensation/', views.dose1_status_save_dispensation, name='dose1_status_save_dispensation'),
        path('dose2_status_save_dispensation/', views.dose2_status_save_dispensation, name='dose2_status_save_dispensation'),
        path('dose3_status_save_dispensation/', views.dose3_status_save_dispensation, name='dose3_status_save_dispensation'),
        path('dose4_status_save_dispensation/', views.dose4_status_save_dispensation, name='dose4_status_save_dispensation'),
    ]
