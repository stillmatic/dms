from checkins.models import Checkin
from checkins.serializers import CheckinSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from checkins.permissions import IsOwner

class CheckinList(generics.ListCreateAPIView):
    queryset = Checkin.objects.all()
    serializer_class = CheckinSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        IsOwner)

    def perform_create(self, serializer):
        serializer.save(check_user=self.request.user)

class CheckinDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Checkin.objects.all()
    serializer_class = CheckinSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
        IsOwner)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer