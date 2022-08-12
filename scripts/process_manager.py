from processManager.models import Process
from django.utils import timezone
import time

#! NOTE : this extension is for checking pending processes.
def run():
    while True:
        if Process.objects.filter(status=Process.PENDING).count() > 0:
            process = sorted(Process.objects.filter(status=Process.PENDING).all(), key=lambda t: t.HRRN)
            process = process[0]
            process.status = Process.STARTED
            process.started_at = timezone.now()
            process.save()
            while process.process_time_sec != 0:
                time.sleep(1)
                process.process_time_sec = process.process_time_sec - 1
            process.status = Process.FINISHED
            process.save()
        else:
            time.sleep(10)


        
        