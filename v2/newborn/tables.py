import django_tables2 as tables
from .models import Newborn

class NewbornTable(tables.Table):
    class Meta:
        model = Newborn
        sequence = ('name', 'age_in_days', 'diagnosis',)
        exclude =('id', 'date_of_birth', 'admission_date', 'gestation_age',)
        attrs = {"class": "table table-striped table-hover rounded", "th": {"class": "text-danger bg-dark text-light", "style": "height: 100px;"}}
    details = tables.TemplateColumn('<a href="http://127.0.0.1:8000/newborn/print/{{record.pk}}/">details</a>', orderable=False)
