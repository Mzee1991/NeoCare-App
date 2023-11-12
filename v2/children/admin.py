from django.contrib import admin
from .models import Registration, Measurements, LabRequestChildren, LabResultChildren

admin.site.register(Registration)
admin.site.register(Measurements)
admin.site.register(LabRequestChildren)
admin.site.register(LabResultChildren)
