import django_filters as filters
from .models import *


class TeamFilter(filters.FilterSet):
    name = filters.CharFilter(label='поиск по командам', field_name='name', lookup_expr='icontains')

    class Meta:
        model = Team
        fields = ('name',)
