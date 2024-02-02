from rest_framework import serializers
from django_celery_results.models import TaskResult


class TaskResultSerializer(serializers.ModelSerializer):
    """
    Serializer for the TaskResult model.
    """
    class Meta:
        model = TaskResult
        fields = '__all__'