import django_filters
from pets.models.pet import Pet

class PetFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(
        field_name='status',
        lookup_expr='exact'
    )

    class Meta:
        model = Pet
        fields = ['status']