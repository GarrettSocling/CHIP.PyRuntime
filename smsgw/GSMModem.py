import os
if os.name == "nt":
    import smsgw.CHIP_IO.GPIO as GPIO
else:
    import CHIP_IO.GPIO as GPIO
from time import sleep
import serial
import smsgw.PDU

hex_string = "07919761989901F00406D04DEA1400088011012100000872041E044104420430043204300439044204350441044C0020043D0430002004410432044F043704380021002004110430043B0430043D0441002004120430044804350433043E0020044104470435044204300020043F043E0020043D043E043C0435044004430020002A0031003000300023"
data = smsgw.PDU.decodeSmsPdu(hex_string)
GPIO.cleanup()

class GSMModemClass():
    port = None
    def __init__(self,tty):
        self.port=serial.Serial(tty)
        self.port.timeout=2
        if self.isOn() == False:
            self.poweron()
        response = self.sendCommand("AT+CMGF=0\r")
        pass
    def process(self):
        response = self.sendCommand("AT+CMGL=4\r")
        pass
    def isOn(self):
        response=self.sendCommand("AT\r")
        return len(response) != 0
    def sendCommand(self,cmd):
        self.port.write(cmd.encode())
        echo=self.port.readline()
        response = ""
        while 1:
            line = self.port.readline().decode()
            response=response + line
            if line == '':
                break
        return response
    def poweron(self):
        GPIO.cleanup()
        try:
            GPIO.setup("XIO-P0",GPIO.OUT)
        except RuntimeError as err:
            print(err)
        GPIO.output("XIO-P0", GPIO.LOW)
        sleep(1)
        GPIO.output("XIO-P0", GPIO.HIGH)
        sleep(1)
        GPIO.output("XIO-P0", GPIO.LOW)
        sleep(2)
        GPIO.cleanup()
