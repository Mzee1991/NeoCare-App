from django.urls import path
from newborn import views

urlpatterns = [
    path('create/', views.CreateView.as_view(), name='create'),
]
