from django.contrib import admin
from .models import NewbornAdmission, MotherDetails, MotherLocation

admin.site.register(NewbornAdmission)
admin.site.register(MotherDetails)
admin.site.register(MotherLocation)
