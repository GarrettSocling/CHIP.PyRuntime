from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^listInbox$', views.listInbox, name='listInbox')
]

from smsgw.GSMModem import GSMModemClass
from threading import Thread
from time import sleep
import os


def modem_thread():
    sleep(5)
    if (os.name == "nt"):
        modem = GSMModemClass('COM3')
    else:
        modem = GSMModemClass('/dev/ttyS0')
    while 1:
        modem.process()
        sleep(1)

MODEMTHREAD=Thread(target=modem_thread)
MODEMTHREAD.start()