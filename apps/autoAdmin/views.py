import logging
from rest_framework.generics import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import GameInfo
from .serializer import GameInfoSerializer
from .filters import GameInfoFilter
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

    def get(self, request):
        return Response('hello')


class ChannelViewSet(viewsets.ModelViewSet):
    queryset = GameInfo.objects.all()
    serializer_class = GameInfoSerializer
    pagination_class = BasePagination
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_class = GameInfoFilter
    ordering_fields = ("id",)
    search_fields = ("name", "game_type", "game_num", "status", "environment")
