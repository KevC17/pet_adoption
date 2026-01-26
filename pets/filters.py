import django_filters
from pets.models.pet import Pet

class PetFilter(django_filters.FilterSet):
    shelter = django_filters.NumberFilter(field_name='shelter__id')
    
    class Meta:
        model = Pet
        fields = ['shelter']