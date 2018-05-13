from control.models import Light
from rest_framework import serializers


class LightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Light
        fields = (
            'pk', 'name',
            'red', 'green', 'blue', 'is_on'
        )
        read_only_fields = (
            'pk', 'name',
        )
