from rest_framework import serializers
from checkins.models import Checkin
from django.contrib.auth.models import User

class CheckinSerializer(serializers.HyperlinkedModelSerializer):
    check_user = serializers.ReadOnlyField(source='check_user.username')
    class Meta:
        model = Checkin
        fields = ('check_user', 'check_msg')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    checkins = serializers.HyperlinkedRelatedField(many=True,
        view_name='checkin-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'checkins')