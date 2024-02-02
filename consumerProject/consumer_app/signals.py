"""from celery.signals import task_postrun
from django.dispatch import receiver
import requests


@receiver(task_postrun)
def send_task_result_to_producer(sender, task_id, task, args, kwargs, **kwds):
    # Retrieve the task result from the database
    result = AsyncResult(task_id).result

    # Send the result to the producer's webhook URL
    producer_webhook_url = 'http://127.0.0.1:8000/api/webhook/'  
    requests.post(producer_webhook_url, json={'result': result})"""