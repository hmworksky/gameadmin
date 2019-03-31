import logging
from rest_framework.generics import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import GameInfo, ProjectInfo
from .serializer import GameInfoSerializer, ProjectInfoSerializer
from .filters import GameInfoFilter, ProjectInfoFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response


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
