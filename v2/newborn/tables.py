import django_tables2 as tables
from .models import Newborn

class NewbornTable(tables.Table):
    class Meta:
        model = Newborn
        sequence = ('name', 'age_in_days', 'diagnosis', 'discharge_date',)
        exclude =('id', 'date_of_birth', 'admission_date', 'gestation_age',)
        attrs = {"class": "table table-striped table-hover"}
