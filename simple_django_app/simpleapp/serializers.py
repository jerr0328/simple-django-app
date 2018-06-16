from rest_framework import serializers

from simple_django_app.simpleapp.models import Pet


class PetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'
