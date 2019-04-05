from rest_framework import serializers
from .models import GameInfo, Channel, ProjectInfo, Article, Task, Phone


class GameInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameInfo
        fields = "__all__"


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = "__all__"


class ProjectInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectInfo
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "user_id", "content", "game", "status", "article_type")


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = "__all__"
