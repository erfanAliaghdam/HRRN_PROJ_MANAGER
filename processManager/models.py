from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone



class Process(models.Model):
    PENDING = 'P'
    STARTED = 'S'
    FINISHED = 'F'
    STATUS = (
        ('P', 'Pending'),
        ('S', 'Started'),
        ('F', 'Finished'),
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='processes', blank=True, null=True)
    process_time_sec = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    status     = models.CharField(choices=STATUS, max_length=1, default=PENDING)
    started_at = models.DateTimeField(blank=True, null=True)
    @property
    def HRRN(self):
        if self.process_time_sec == 0:
            return 0
        else:
            dur = timezone.now() - self.created_at  
            return (self.process_time_sec + dur.total_seconds() ) / self.process_time_sec