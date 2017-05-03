"""Get wifi info"""
import os
from subprocess import Popen, PIPE

class WiFi():
    """Info about wifi"""
    def __init__(self):
        self.ip = 'n/a'
        self.nets = []
        if os.name == "nt":
            self.script = "wifi.bat"
        else:
            self.script = "./wifi.sh"
    def getInfo(self):
        """Get info from bash script"""
        process = Popen(self.script, stdout=PIPE, shell=True)
        (output, err) = process.communicate()
        exit_code = process.wait()
        output = output.decode("utf-8")
        lines = output.split(os.linesep)
        self.ip = lines[0].strip()
        for i in range(2,len(lines)-3):
            self.nets.append(WifiNet(lines[i]))

class WifiNet():
    """Network info"""
    def __init__(self,name):
        self.name = name
        self.signal=""
        self.rate=""
        self.security=""
