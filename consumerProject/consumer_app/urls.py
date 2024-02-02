from django.urls import path, include
from .views import process_message
from rest_framework.routers import DefaultRouter
from .views import TaskResultViewSet


router = DefaultRouter()
router.register(r'task_results', TaskResultViewSet)

urlpatterns = [
    path('', process_message, name='process_message'),
    path('', include(router.urls)),
]