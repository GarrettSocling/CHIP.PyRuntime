""""""
import os
from subprocess import Popen, PIPE

class Battery():
    """"""
    def __init__(self):
        self.voltage = 'n/a'
        self.percent = 'n/a'
        self.charging = 'n/a'
        self.drain = 'n/a'
        self.temp = 'n/a'
        if os.name == "nt":
            self.script = "battery.bat"
        else:
            self.script = "./battery.sh"
    def getInfo(self):
        """"""
        process = Popen(self.script, stdout=PIPE, shell=True)
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
