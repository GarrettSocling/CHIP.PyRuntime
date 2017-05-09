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
        for i in range(2, len(lines)-3):
            self.nets.append(WifiNet(lines[i]))
    def connect(self,net,pwd):
        cmd = "nmcli d wifi connect "+net+" password "+pwd
        if os.name == "nt":
            return
        process = Popen(cmd, stdout=PIPE, shell=True)
        (output, err) = process.communicate()
        exit_code = process.wait()
class WifiNet():
    """Network info"""
    def __init__(self, raw):
        elems = raw.split(' ')
        elems = list(filter(None, elems))
        if elems[0] == "*":
            ind = elems.index("Infra")
            self.name = ' '.join(elems[1:ind])
            self.signal = elems[ind+4]
            self.rate = elems[ind+2]
            self.security = ' '.join(elems[ind+6:len(elems)])
            self.connected = True
        else:
            ind = elems.index("Infra")
            self.name = ' '.join(elems[0:ind])
            self.signal = elems[ind+4]
            self.rate = elems[ind+2]
            self.security = ' '.join(elems[ind+6:len(elems)])
            self.connected = False
