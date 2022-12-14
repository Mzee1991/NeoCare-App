from newborn.models import Newborn
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.views import generic


class CreateView(generic.edit.CreateView):
    model = Newborn
    fields = ["name", "admission_date", "gestation_age", "diagnosis", "discharge_date"]
    
    def get_form(self):
        form = super().get_form()
        
        form.fields["admission_date"].widget = DatePickerInput(
            attrs={"class": "form-control"},
            options={
                "format": "YYYY-MM-DD",
                "showTodayButton": False,
            },
        )
        
        form.fields["discharge_date"].widget = DatePickerInput(
            attrs={"class": "form-control"},
            options={
                "format": "YYYY-MM-DD",
                "showTodayButton": False,
            },
        )
        return form
