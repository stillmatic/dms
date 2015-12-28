from rest_framework import serializers
from checkins.models import Checkin
from django.contrib.auth.models import User

class CheckinSerializer(serializers.ModelSerializer):
    check_user = serializers.ReadOnlyField(source='check_user.username')
    class Meta:
        model = Checkin
        fields = ('check_user', 'check_msg')

class UserSerializer(serializers.ModelSerializer):
    checkins = serializers.PrimaryKeyRelatedField(many=True,
     queryset=Checkin.objects.all())

    class Meta:
        model = User
        fields = ('id', 'email', 'checkins')