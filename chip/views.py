from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
import os
from subprocess import Popen, PIPE

# Create your views here.

class BatteryInfo():
    def __init__(self):
        self.voltage = 'Error'
        if os.name=="nt":
            self.script = "battery.bat"
        else:
            self.script = "./battery.sh"
    def getInfo(self):
        process = Popen(self.script, stdout=PIPE,shell=True)
        (output, err) = process.communicate()
        exit_code = process.wait()
        output = output.decode("utf-8")
        for kv in output.split(os.linesep):
            keyval = kv.split("=")
            if len(keyval)==2:
                if keyval[0].strip() == 'BAT_VOLT':
                    self.voltage = keyval[1].strip()

def index(request):
    battery = BatteryInfo()
    battery.getInfo()
    template = loader.get_template('chip/index.html')
    context = {
        'battery': battery,
    }
    return HttpResponse(template.render(context, request))

def battery(request):
    battery = BatteryInfo()
    battery.getInfo()
    return JsonResponse({'volts':battery.voltage})