# consumer_project

Clone of the project:
    git clone <url>

Creating Virtual Environments:
    python3 -m venv venv

    - Activate the environment: (windows)
        venv\Scripts\activate

Installing Dependencies:
    pip install django celery django-rest-framework django-celery-results requests

Verification:
    pip list

Creating Django Project:
    django-admin startproject consumerProject

Create app:
    python manage.py startapp consumer_app

Migration:
    python manage.py makemigrations
    python manage.py migrate

Create user:
    python manage.py createsuperuser

Run server:
    python manage.py runserver

Setting up RabbitMQ:
    - To use Celery we need to create a RabbitMQ user, a virtual host and allow that user access to that virtual host:

        Creating a new user via the web interface:
        1. Access the Users page in the RabbitMQ web interface:
        2. Click on the "Create User" button.
        3. Enter the username and password for the user.
        4. Select the virtual hosts on which the user will have privileges.
        5. Click on the "Create" button.
        (Alternative method) Creating a new user via the rabbitmqctl command:
        - Run the following command:
        rabbitmqctl add_user <username> <password>
        - Grant the user permissions to some virtual hosts! See 'rabbitmqctl help set_permissions' to learn more.
            rabbitmqctl set_user_tags username administrator
        - To assign privileges to the user, run the following command:
            rabbitmqctl set_permissions -p <vhost> <username> <configure> <write> <read>
            example: rabbitmqctl set_permissions -p / username ".*" ".*" ".*"
        - Execute this command in cmd:
            rabbitmq-plugins enable rabbitmq_management
        - Open the browser and enter the URL: http://localhost:15672/

Create a Celery Task
Configure Celery
Run the Celery Worker
    celery -A consumerProject worker -l info

    Verify that the consumer receives messages from the producer via the RabbitMQ queue:
    - 1. Open the RabbitMQ management tool.
    - 2. Go to the Queues page.
    - 3. Select the celery_tasks queue.
    - 4. Check that the Messages column contains messages.

Install Django REST Framework:
    pip install djangorestframework

To test the view that accepts a POST request from the producer and calls the Celery task with the request data:
    TEST POSTMAN :
    - process_message 
        url : http://127.0.0.1:8001/process_message/
        select "POST" as the request method
        Go to the "Body" tab, select "raw" and choose "JSON" from the dropdown menu. Enter your JSON payload with the 'text' and 'webhook_url'

To test the API endpoint that exposes the Celery task result to the producer:
    1. To get the token:
        python manage.py shell
        from django.contrib.auth.models import User
        from rest_framework.authtoken.models import Token
        user = User.objects.get(username='example_user')
        token = Token.objects.create(user=user)
        print(token.key)
    2. Test in Postman:
        In Postman, headers should be set separately from the URL 'http://127.0.0.1:8001/process_message/task_results/'. Here's how to correctly set the Authorization header in Postman:
            1. Open Postman and select the request you want to send.
            2. Go to the "Headers" tab.
            3. Add a new header with the key Authorization and the value Token YOUR_TOKEN_HERE, where YOUR_TOKEN_HERE is the actual token you obtained.

To create a signal handler:
    - 1. Install the requests Library:
        pip install requests
    - 2. Create a Signal Handler