from django.http import HttpResponse
from .models import WorkData

def index(request):
    
    data = []    
    data = WorkData.objects.all().values()
    return HttpResponse(data)

    
