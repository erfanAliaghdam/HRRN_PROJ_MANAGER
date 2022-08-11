from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Process(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='processes', blank=True, null=True)
    process_time_sec = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    #! started?
    #! remaining?
