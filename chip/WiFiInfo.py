""""""
import os
from subprocess import Popen, PIPE

class WiFi():
    """"""
    def __init__(self):
        self.ip = 'n/a'
        if os.name == "nt":
            self.script = "wifi.bat"
        else:
            self.script = "./wifi.sh"
    def getInfo(self):
        """"""
        pass
        process = Popen(self.script, stdout=PIPE, shell=True)
        (output, err) = process.communicate()
        exit_code = process.wait()
        output = output.decode("utf-8")
        lines = output.split(os.linesep)
        for kval in output.split(os.linesep):
            pass
        self.ip=lines[0].strip()