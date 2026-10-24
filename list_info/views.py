from rest_framework import generics

from .models import Task, Category
from .serializers import TaskShortSerializer, TaskDetailSerializer, TaskWriteSerializer


class TaskListCreateView(generics.ListCreateAPIView):

    """
    GET  /api/v1/tasks/ — краткий список задач.
    POST /api/v1/tasks/ — создание задачи (category и tags передаются как id).
    """

    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TaskShortSerializer
        return TaskWriteSerializer


class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    """
    GET          /api/v1/tasks/{id}/ — детальный просмотр с вложенными category и tags.
    PUT, PATCH   /api/v1/tasks/{id}/ — обновление задачи.
    DELETE       /api/v1/tasks/{id}/ — удаление задачи.
    """

    queryset = Task.objects.select_related('category').prefetch_related('tags')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TaskDetailSerializer
        return TaskWriteSerializer
