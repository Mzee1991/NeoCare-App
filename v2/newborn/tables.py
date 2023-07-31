import django_tables2 as tables
from .models import NewbornAdmission

class NewbornTable(tables.Table):
    class Meta:
        model = NewbornAdmission
        sequence = ('name',)
        exclude =('id', 'admission_date','place_of_birth','hospital_name','indication','mode_of_delivery','resuscitation_done',
                'resuscitation_choices_1', 'resuscitation_choices_2', 'facility_name', 'referral_date_time', 'reason_for_referral',
                'means_of_transport','oxygen_transport',)
        attrs = {"class": "table table-striped table-hover rounded", "th": {"class": "text-danger bg-dark text-light", "style": "height: 100px;"}}
    details = tables.TemplateColumn('<a href="http://127.0.0.1:8000/newborn/print/{{record.pk}}/">details</a>', orderable=False)
