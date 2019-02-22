from django.http import HttpResponse
from .models import WorkData
from django.core import serializers

def index(request):
    
    return HttpResponse(serializers.serialize("json", WorkData.objects.all()))

