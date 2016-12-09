from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from chip.BatteryInfo import Battery

# Create your views here.

def index(request):
    """Return index page with status info"""
    batt = Battery()
    batt.getInfo()
    context = {
        'battery': batt,
    }
    return render(request, 'chip/index.html', context)

def battery(request):
    """Return JSON object with battery info"""
    batt = Battery()
    batt.getInfo()
    return JsonResponse(
        {"volts":batt.voltage,
         "percent":batt.percent,
         "charging":batt.charging,
         "drain":batt.drain,
         "temp":batt.temp})
