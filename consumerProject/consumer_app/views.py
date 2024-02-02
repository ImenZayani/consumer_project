from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import process_data
from rest_framework import viewsets, permissions
from django_celery_results.models import TaskResult
from .serializers import TaskResultSerializer
from rest_framework.authentication import TokenAuthentication


@api_view(['POST'])
def process_message(request):
    """
    Accepts a POST request from the producer, triggers a Celery task to 
    process the message, and returns the task ID.

    Expects a JSON payload with 'text' and 'webhook_url' fields.
    """
    data = request.data
    text = data.get('text')
    webhook_url = data.get('webhook_url')

    if text and webhook_url:
        task = process_data.delay(text, webhook_url)
        return Response({'task_id': task.id}, status=202)
    else:
        return Response({'error': 'Invalid data'}, status=400)
 
    
class TaskResultViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for the TaskResult model.
    """
    queryset = TaskResult.objects.all()
    serializer_class = TaskResultSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]