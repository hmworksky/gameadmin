from rest_framework import viewsets
from rest_framework import pagination
from apps.autoAdmin import models as am
from apps.autoAdmin import serializer as auto_serializ
from apps.autoAdmin import filters as af
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter


class LimitSet(pagination.LimitOffsetPagination):
    # 每页默认几条
    default_limit = 10
    # 设置传入页码数参数名
    page_query_param = "page"
    # 设置传入条数参数名
    limit_query_param = 'limit'
    # 设置传入位置参数名
    offset_query_param = 'offset'
    # 最大每页显示条数
    max_limit = None


class BasePagination(pagination.PageNumberPagination):
    page_size = 10
    page_query_param = 'p'
    max_page_size = 20


class BaseViewSet(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    ordering_fields = ("id",)
    pagination_class = LimitSet


class InterfaceInfoViewSet(BaseViewSet):
    queryset = am.InterfaceInfo.objects.all()
    serializer_class = auto_serializ.InterfaceInfoSerializer
    filter_class = af.InterfaceInfoFilter
    search_fields = filter_class.get_fields()


class GameInfoViewSet(BaseViewSet):
    queryset = am.GameInfo.objects.all()
    serializer_class = auto_serializ.GameInfoSerializer
    filter_class = af.GameInfoFilter
    search_fields = ("name", "game_type", "game_num", "status", "environment")


class ProjectInfoViewSet(BaseViewSet):
    queryset = am.ProjectInfo.objects.all()
    serializer_class = auto_serializ.ProjectInfoSerializer
    filter_class = af.ProjectInfoFilter
    search_fields = ("project_name", )


class TaskViewSet(BaseViewSet):
    queryset = am.Task.objects.all()
    serializer_class = auto_serializ.TaskSerializer
    filter_class = af.TaskFilter
    search_fields = ("name", )


class ArticleViewSet(BaseViewSet):
    queryset = am.Article.objects.all()
    serializer_class = auto_serializ.ArticleSerializer
    filter_class = af.ArticleFilter
    search_fields = ("title", "content")


class PhoneViewSet(BaseViewSet):
    queryset = am.Phone.objects.all()
    serializer_class = auto_serializ.PhoneSerializer
    filter_class = af.PhoneFilter
    search_fields = ("name", "version")


class MockServerViewSet(BaseViewSet):
    queryset = am.MockServer.objects.all()
    serializer_class = auto_serializ.MockServerSerializer
    filter_class = af.MockServerFilter
    search_fields = ("name", "url_info")
