from checkins.models import Checkin
from checkins.serializers import CheckinSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CheckinList(APIView):
    """
    List all Checkins, or create a new Checkin.
    """
    def get(self, request, format=None):
        Checkins = Checkin.objects.all()
        serializer = CheckinSerializer(Checkins, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CheckinSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CheckinDetail(APIView):
    """
    Retrieve, update or delete a Checkin instance.
    """
    def get_object(self, pk):
        try:
            return Checkin.objects.get(pk=pk)
        except Checkin.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Checkin = self.get_object(pk)
        serializer = CheckinSerializer(Checkin)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Checkin = self.get_object(pk)
        serializer = CheckinSerializer(Checkin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Checkin = self.get_object(pk)
        Checkin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)