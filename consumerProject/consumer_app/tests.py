from django.test import TestCase
from celery.signals import task_postrun
from rest_framework.test import APIClient
from django_celery_results.models import TaskResult
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from unittest.mock import patch
from .tasks import process_data


class TaskResultViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Generate a token for the user
        self.token = Token.objects.create(user=self.user)
        # Create a TaskResult object for testing
        self.task_result = TaskResult.objects.create(task_id='test-task-id', status='SUCCESS', result='Test result')
        self.list_url = '/process_message/task_results/'
        self.detail_url = f'/process_message/task_results/{self.task_result.pk}/'

    def test_list_view(self):
        """
        Test retrieving a list of task results.
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test result')

    def test_detail_view(self):
        """
        Test retrieving a single task result.
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test result')
        
"""class SignalHandlerTests(TestCase):

    @patch('requests.post')  # Mock the requests.post call to avoid external HTTP requests
    def test_task_result_signal_triggers_webhook(self, mock_post):
        task_id = 'test_task_id'
        result = 'Test result'

        # Simulate task completion and signal emission
        task_postrun.send(sender=None, task_id=task_id, task=process_data, args=[], kwargs={}, **{})

        # Assert that the signal handler was called and sent the correct data to the webhook
        mock_post.assert_called_once_with(
            'http://127.0.0.1:8000/api/webhook/', 
            json={'result': result}
        )"""