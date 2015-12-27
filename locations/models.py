from django.db import models
from django.conf import settings
from datetime import datetime

# Create your models here.
class Checkin(models.Model):
  check_user = models.ForeignKey(settings.AUTH_USER_MODEL)
  check_time = models.DateTimeField('User checkin date/time',
    default=datetime.now, blank=True)
  check_msg = models.CharField(max_length=140)

