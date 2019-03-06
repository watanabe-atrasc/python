from django.http import HttpResponse
from .models import WorkData
from .models import SyainData
from django.core import serializers
from django.http.response import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import datetime


def GetInfo(request):
    return HttpResponse(serializers.serialize('json', WorkData.objects.all()))

def Login(request):
    try:
        
        status = {"status":0}
        
        if (request.method == 'GET'):
            SyainId = request.GET['id']
            password = request.GET['password']
            SyainDataKey = SyainData.objects.get(SyainId=SyainId)     
            if (SyainDataKey.PassWord == password):
                status['status'] = 0
            else:
                status['status'] = 1
    except ObjectDoesNotExist:
        status['status'] = 2
    except:
        status['status'] = 99
    finally:
        return JsonResponse(status)
    
def Record(request):
    try:
        
        status = {"status":0}
        
        if (request.method == 'GET'):
            
            SyainId = request.GET['id']
            date = request.GET['date']
            type = request.GET['type']
            
            if (type == '1'):
                WorkData.objects.create(SyainId=SyainId, date=datetime.date.today(), StartTime=datetime.datetime.now(), MorningOffFlg=False, AfternoonOffFlg=False)
                status['status'] = 0
            elif (type == '2'):
                WorkDataKey =WorkData.objects.filter(SyainId=SyainId, date=date).first()
                dt_now = datetime.datetime.now()      
                dt = datetime.datetime(dt_now.year, dt_now.month, dt_now.day, 17, 45, 00, 000000)
                WorkDataKey.EndTime = dt                
                WorkDataKey.save()
                status['status'] = 0
            elif (type == '3'):
                WorkDataKey =WorkData.objects.filter(SyainId=SyainId, date=date).first()
                WorkDataKey.EndTime = datetime.datetime.now()                
                WorkDataKey.save()
                status['status'] = 0
            elif (type == '4'):
                dt_now = datetime.datetime.now()      
                dt = datetime.datetime(dt_now.year, dt_now.month, dt_now.day, 9, 00, 00, 000000)
                WorkData.objects.create(SyainId=SyainId, date=datetime.date.today(), StartTime=dt, MorningOffFlg=True, AfternoonOffFlg=False)
                status['status'] = 0
            elif (type == '5'):
                WorkDataKey =WorkData.objects.filter(SyainId=SyainId, date=date).first()                
                dt_now = datetime.datetime.now()      
                dt = datetime.datetime(dt_now.year, dt_now.month, dt_now.day, 17, 45, 00, 000000)
                WorkDataKey.EndTime = dt  
                WorkDataKey.AfternoonOffFlg = True
                WorkDataKey.save()
                status['status'] = 0
            else:
                status['status'] = 2
    except:
        status['status'] = 99
    finally:
        return JsonResponse(status)
    