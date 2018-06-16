from rest_framework import viewsets

from simple_django_app.simpleapp.models import Pet
from simple_django_app.simpleapp.serializers import PetSerializer


class PetViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Look at all the pets!
    """
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
