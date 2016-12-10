import os
if os.name == "nt":
    import smsgw.CHIP_IO.GPIO as GPIO
else:
    import CHIP_IO.GPIO as GPIO
from time import sleep
import serial
import smsgw.PDU
from .models import InboxSMS

hex_string = "07919761989901F00406D04DEA1400088011012100000872041E044104420430043204300439044204350441044C0020043D0430002004410432044F043704380021002004110430043B0430043D0441002004120430044804350433043E0020044104470435044204300020043F043E0020043D043E043C0435044004430020002A0031003000300023"
data = smsgw.PDU.decodeSmsPdu(hex_string)
send = smsgw.PDU.encodeSmsSubmitPdu("+79806843757","Тест",requestStatusReport=False)
GPIO.cleanup()

class GSMModemClass():
    """Class for interaction with SIM900"""
    port = None
    def __init__(self, tty):
        self.port = serial.Serial(tty)
        self.port.timeout = 2
        if self.ison() is False:
            self.switchpower()
        self.sendcommand("AT+CMGF=0\r")
    def process(self):
        """All operations with modem"""
        response = self.sendcommand("AT+CMGL=4\r")
        lines = response.split("\r\n")
        while "" in lines: lines.remove("")
        while "OK" in lines: lines.remove("OK")
        for word in lines[:]:
            if word.startswith(("+CMTI:","RING")):
                lines.remove(word)
        i=0
        while i<len(lines)/2:
            try:
                smsid = lines[i*2].split(": ")[1].split(",")[0]
                pdu = lines[i*2+1]
                parsedsms = smsgw.PDU.decodeSmsPdu(pdu)
                i+=1
                sms = InboxSMS(sender=parsedsms["number"], received_date=parsedsms["time"],text=parsedsms["text"])
                print("Receved sms from ("+sms.sender+") " + sms.text)
                sms.save()
                self.sendcommand("AT+CMGD="+smsid+"\r")
            except Exception as err:
                print(err)
                i+=1
    def ison(self):
        """Check modem response"""
        response = self.sendcommand("AT\r")
        return len(response) != 0
    def sendcommand(self, cmd):
        """Send command and read all output"""
        self.port.write(cmd.encode())
        self.port.readline()
        response = ""
        while 1:
            line = self.port.readline().decode()
            response = response + line
            if line == '':
                break
        return response
    def switchpower(self):
        """Send power on/off impulse on GPIO pin"""
        GPIO.cleanup()
        try:
            GPIO.setup("XIO-P0", GPIO.OUT)
        except RuntimeError as err:
            print(err)
        GPIO.output("XIO-P0", GPIO.LOW)
        sleep(1)
        GPIO.output("XIO-P0", GPIO.HIGH)
        sleep(1)
        GPIO.output("XIO-P0", GPIO.LOW)
        sleep(2)
        GPIO.cleanup()
