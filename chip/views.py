from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

class BatteryInfo():
    def __init__(self, voltage,discharge):
        self.voltage = voltage
        self.discharge = discharge



def index(request):
    volts = 'Error'
    discharge = 'Error'
    import os
    from subprocess import Popen, PIPE
    if os.name=="nt":
        script = "battery.bat"
    else:
        script = "/usr/bin/battery.sh"
    process = Popen(script, stdout=PIPE,shell=True)
    (output, err) = process.communicate()
    exit_code = process.wait()
    output = output.decode("utf-8")
    for kv in output.split(os.linesep):
        keyval = kv.split("=")
        if len(keyval)==2:
            if keyval[0].strip() == 'Battery voltage':
                volts = keyval[1].strip()
            if keyval[0].strip() == 'Battery discharge current':
                discharge = keyval[1].strip()
    bat = BatteryInfo(volts,discharge)
    template = loader.get_template('chip/index.html')
    context = {
        'bat': bat,
    }
    return HttpResponse(template.render(context, request))
