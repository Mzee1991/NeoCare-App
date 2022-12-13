from django.db import models

class Newborn(models.Model):
    name = models.CharField(max_length=50)
    admission_date = models.DateField()
    gestation_age = models.IntegerField(default=28)
    diagnosis = models.CharField(max_length=100)
    discharge_date =models.DateField()

    def __str__(self):
        return self.name + ': ' + self.diagnosis

    class Meta:
        ordering = ['admission_date']
