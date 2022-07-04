from django.utils import timezone
from .models import Task
from celery import shared_task


@shared_task
def change_task_status():
    current_date = timezone.now()
    return Task.objects.filter(
        created__lt=current_date).update(status='Delayed')
