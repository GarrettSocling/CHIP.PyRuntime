from django.db import models

# Create your models here.

class InboxSMS(models.Model):
    # Inbound sms model
    sender = models.CharField(max_length=20)
    received_date = models.DateTimeField()
    text = models.CharField(max_length=1024)
    def __str__(self):
        return self.received_date.__str__()+" from "+self.sender+":"+self.text
