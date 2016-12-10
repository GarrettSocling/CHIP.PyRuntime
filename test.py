#!/usr/bin/env python
import os
from subprocess import Popen, PIPE
import CHIP_IO.GPIO as GPIO
from time import sleep

if os.name=="nt":
    script = "battery.bat"
else:
    script = "battery.sh"
process = Popen(script, stdout=PIPE,shell=True)
(output, err) = process.communicate()
exit_code = process.wait()
output = output.decode("utf-8") 
for kv in output.split("\r\n"):
    keyval = kv.split("=")
    if len(keyval)==2:
        print(keyval[0]+"="+keyval[1])
#print(output.split("\r\n"))
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