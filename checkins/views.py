from checkins.models import Checkin
from checkins.serializers import CheckinSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from checkins.permissions import IsOwner
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

class CheckinList(generics.ListCreateAPIView):
    #queryset = Checkin.objects.all()
    serializer_class = CheckinSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Checkin.objects.filter(check_user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(check_user=self.request.user)

class CheckinDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Checkin.objects.all()
    serializer_class = CheckinSerializer
    permission_classes = (permissions.IsAdminUser, IsOwner)


class UserList(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return User.objects.filter(username=self.request.user)

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser, IsOwner)


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'checkins': reverse('checkin-list', request=request, format=format)
    })