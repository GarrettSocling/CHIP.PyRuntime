from django.apps import AppConfig

class SmsgwConfig(AppConfig):
    name = 'smsgw'
    name_menu = "Смс шлюз"

from smsgw.GSMModem import GSMModemClass
from threading import Thread
from time import sleep
import os

modem=None
if (modem==None):
    if (os.name == "nt"):
        modem = GSMModemClass('COM3')
    else:
        modem = GSMModemClass('/dev/ttyS0')

def modem_thread():
    while 1:
        modem.process()
        sleep(1)

MODEMTHREAD=Thread(target=modem_thread)
MODEMTHREAD.start()
