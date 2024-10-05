from rest_framework import serializers
from .models import Cats, Breeds


class CatsSerializer(serializers.ModelSerializer):
    breed = serializers.SlugRelatedField(queryset=Breeds.objects.all(), slug_field='breed')
    owner=serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Cats
        fields = ('name','color','age','description','owner','breed')


