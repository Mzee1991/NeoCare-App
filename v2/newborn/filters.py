from .models import Newborn
import django_filters

class NewbornFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Newborn
        fields = ['name', 'mother']
