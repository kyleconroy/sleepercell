from django.db import models
from django.contrib.auth.models import User

AWAKE = 1
ASLEEP = 0
STATE_CHOICES = (
    (AWAKE, 'Awake'),
    (ASLEEP, 'Asleep'),
)

class SleepState(models.Model):

    user  = models.ForeignKey(User)
    state = models.IntegerField(choices=STATE_CHOICES)
    start = models.DateTimeField(auto_now_add=True)
    end   = models.DateTimeField(null=True, blank=True)

    def is_awake(self):
        return self.state == AWAKE

    def is_asleep(self):
        return self.state == ASLEEP

    def __unicode__(self):
        return str(self.state) + " " + str(self.date)


