from rest_framework import serializers
from .models import Task


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "name"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "name"]


class TaskShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "status", "created_date"]


class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "status", "created_date", "category", "tags"]


class TaskWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "category", "tags"]