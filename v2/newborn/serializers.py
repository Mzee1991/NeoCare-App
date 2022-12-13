from rest_framework import serializers
from .models import Newborn

class NewbornSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newborn
        fields = ['id', 'name', 'admission_date', 'gestation_age', 'diagnosis', 'discharge_date']
