from celery import shared_task
from django_celery_results.models import TaskResult
from requests import post


@shared_task
def process_data(text, webhook_url):
    """
    
    Processes the given text by reversing it and counting the number of words.
    Sends the result back to the producer via the provided webhook URL.

    Args:
        text (str): The text to be processed.
        webhook_url (str): The URL to send the result back to the producer.

    Returns:
        str: A string indicating the processed text and the word count.
    """
    reversed_text = text[::-1]
    word_count = len(text.split())

    # Store the result in the Django database
    result = TaskResult.objects.create(result=str(word_count))

    # Send the result back to the producer via the webhook URL
    post(webhook_url, json={'result': str(word_count)})

    return f'Processed text: "{reversed_text}", Word count: {word_count}'