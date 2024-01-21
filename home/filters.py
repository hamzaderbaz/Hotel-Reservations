import django_filters
from property.models import Property

class PropertyFilter(django_filters.FilterSet):
    class Meta:
        model = Property
        fields = ['name', 'category']


class PropertySearchFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', field_name='name')
    location = django_filters.CharFilter(lookup_expr='icontains', field_name='place__name')

    class Meta:
        model = Property
        fields = ['name', 'location']