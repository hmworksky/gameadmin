from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import GameInfo, ProjectInfo, Task, Article, Phone
from .serializer import GameInfoSerializer, ProjectInfoSerializer, TaskSerializer, ArticleSerializer, PhoneSerializer
from .filters import GameInfoFilter, ProjectInfoFilter, TaskFilter, ArticleFilter, PhoneFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter


class BasePagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'p'
    max_page_size = 20


class GameInfoViewSet(viewsets.ModelViewSet):
    queryset = GameInfo.objects.all()
    serializer_class = GameInfoSerializer
    pagination_class = BasePagination
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_class = GameInfoFilter
    ordering_fields = ("id", )
    search_fields = ("name", "game_type", "game_num", "status", "environment")


class ChannelViewSet(viewsets.ModelViewSet):
    queryset = GameInfo.objects.all()
    serializer_class = GameInfoSerializer
    pagination_class = BasePagination
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_class = GameInfoFilter
    ordering_fields = ("id",)
    search_fields = ("name", "game_type", "game_num", "status", "environment")


class ProjectInfoViewSet(viewsets.ModelViewSet):
    queryset = ProjectInfo.objects.all()
    serializer_class = ProjectInfoSerializer
    pagination_class = BasePagination
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_class = ProjectInfoFilter
    ordering_fields = ("id",)
    search_fields = ("project_name", )


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = BasePagination
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_class = TaskFilter
    ordering_fields = ("id",)
    search_fields = ("name", )


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = BasePagination
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_class = ArticleFilter
    ordering_fields = ("id",)
    search_fields = ("title", "content")


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    pagination_class = BasePagination
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_class = PhoneFilter
    ordering_fields = ("id",)
    search_fields = ("name", "version")
