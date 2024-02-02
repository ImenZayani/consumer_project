from django.apps import AppConfig


class ConsumerAppConfig(AppConfig):
    name = 'consumer_app'

"""     def ready(self):
        from .signals import send_task_result_to_producer
        task_postrun.connect(send_task_result_to_producer)"""