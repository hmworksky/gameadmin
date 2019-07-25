from rest_framework import serializers
from apps.autoAdmin import models as am
# from .models import GameInfo, Channel, ProjectInfo, Article, Task, Phone, InterfaceInfo


class InterfaceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = am.InterfaceInfo
        fields = "__all__"


class GameInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = am.GameInfo
        fields = ['id', 'name', 'game_num', 'game_type', 'status', 'env', 'memo']


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = am.Channel
        fields = "__all__"


class ProjectInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = am.ProjectInfo
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = am.Task
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = am.Article
        fields = ("title", "user_id", "content", "game", "status", "article_type")


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = am.Phone
        fields = "__all__"


class MockServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = am.MockServer
        fields = "__all__"
