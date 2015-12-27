from rest_framework import serializers
from locations.models import Checkin

class CheckinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkin
        fields = ('check_msg')
    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.msg = validated_data.get('title', instance.msg)
        instance.save()
        return instance