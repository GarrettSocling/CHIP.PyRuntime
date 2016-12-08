from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
import os
from subprocess import Popen, PIPE

# Create your views here.

class BatteryInfo():
    def __init__(self):
        self.voltage = 'n/a'
        self.percent = 'n/a'
        self.charging = 'n/a'
        self.drain = 'n/a'
        self.temp = 'n/a'
        if os.name=="nt":
            self.script = "battery.bat"
        else:
            self.script = "./battery.sh"
    def getInfo(self):
        process = Popen(self.script, stdout=PIPE,shell=True)
        (output, err) = process.communicate()
        exit_code = process.wait()
        output = output.decode("utf-8")
        for kval in output.split(os.linesep):
            keyval = kval.split("=")
            if len(keyval) == 2:
                if keyval[0].strip() == 'BAT_VOLT':
                    self.voltage = keyval[1].strip()
                if keyval[0].strip() == 'BAT_GAUGE':
                    self.percent = keyval[1].strip()
                if keyval[0].strip() == 'CHARG_IND':
                    self.charging = keyval[1].strip()
                if keyval[0].strip() == 'BAT_DRAIN':
                    self.drain = keyval[1].strip()
                if keyval[0].strip() == 'TEMP':
                    self.temp = keyval[1].strip()

def index(request):
    batt = BatteryInfo()
    batt.getInfo()
    template = loader.get_template('chip/index.html')
    context = {
        'battery': batt,
    }
    return HttpResponse(template.render(context, request))

def battery(request):
    batt = BatteryInfo()
    batt.getInfo()
    return JsonResponse({'volts':batt.voltage, 
    "percent":batt.percent, 
    "charging":batt.charging, 
    "drain":batt.drain, 
    "temp":batt.temp})
