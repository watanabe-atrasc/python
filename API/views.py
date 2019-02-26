from django.http import HttpResponse
from .models import WorkData
from .models import SyainData
from django.core import serializers
from django.http.response import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

def SyainSelect(request):
    return HttpResponse(serializers.serialize('json', WorkData.objects.all()))

def Login(request):
    try:
        data = {"status":0}
        if (request.method == 'GET'):
            id = request.GET['id']
            password = request.GET['password']
            item = SyainData.objects.get(SyainId=id)     
            if (item.PassWord == password):
                data['status'] = 0
            else:
                data['status'] = 1
    except ObjectDoesNotExist:
        data['status'] = 2
    except:
        data['status'] = 99
    finally:
        return JsonResponse(data)