from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from locations.models import Checkin
from locations.serializers import CheckinSerializer

# Create your views here.
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def checkin_list(request):
    """
    List all checkins, or create a new checkin.
    """
    if request.method == 'GET':
        checkins = Checkin.objects.all()
        serializer = CheckinSerializer(checkins, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CheckinSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def checkin_detail(request, pk):
    """
    Retrieve, update or delete a checkin.
    """
    try:
        checkin = checkin.objects.get(pk=pk)
    except checkin.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CheckinSerializer(checkin)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CheckinSerializer(checkin, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        checkin.delete()
        return HttpResponse(status=204)