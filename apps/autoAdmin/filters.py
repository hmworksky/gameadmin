from django_filters import rest_framework as rf
from apps.autoAdmin import models as am
# from .models import GameInfo, Channel, ProjectInfo, Task, Article, Phone, InterfaceInfo


class InterfaceInfoFilter(rf.FilterSet):
    app_name = rf.ChoiceFilter(choices=am.InterfaceInfo.INTERFACE_APP)
    request_method = rf.ChoiceFilter(choices=am.InterfaceInfo.INTERFACE_REQUEST_METHOD)
    request_protocol = rf.ChoiceFilter(choices=am.InterfaceInfo.INTERFACE_REQUEST_PROTOCOL)
    name = rf.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = am.InterfaceInfo
        fields = ["app_name", "request_method", "request_protocol", "name"]


class GameInfoFilter(rf.FilterSet):
    game_type = rf.ChoiceFilter(choices=am.GameInfo.GAME_TYPE)
    env = rf.ChoiceFilter(choices=am.GameInfo.GAME_ENV)
    status = rf.ChoiceFilter(choices=am.GameInfo.GAME_STATUS)
    name = rf.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = am.GameInfo
        fields = ["game_type", "env", "status", "name"]


class ProjectInfoFilter(rf.FilterSet):
    project_name = rf.CharFilter(field_name="project_name")
    responsible_name = rf.CharFilter(field_name="responsible_name")
    status = rf.NumberFilter(field_name="status")

    class Meta:
        model = am.ProjectInfo
        fields = ["project_name", "responsible_name", "status"]


class TaskFilter(rf.FilterSet):
    name = rf.CharFilter(field_name="name", lookup_expr="icontains")
    task_id = rf.CharFilter(field_name="task_id")
    status = rf.NumberFilter(field_name="status")
    user = rf.CharFilter(field_name="user", lookup_expr="icontains")
    create_time = rf.DateTimeFilter(field_name="create_time", lookup_expr="gte")

    class Meta:
        model = am.Task
        fields = ["name", "task_id", "status", "user", "create_time"]


class ArticleFilter(rf.FilterSet):
    title = rf.CharFilter(field_name="title", lookup_expr="icontains")
    user_id = rf.CharFilter(field_name="user_id", lookup_expr="icontains")
    game = rf.CharFilter(field_name="game")
    status = rf.NumberFilter(field_name="status")
    content = rf.CharFilter(field_name="content", lookup_expr="icontains")
    article_type = rf.NumberFilter(field_name="article_type")
    create_time = rf.DateTimeFilter(field_name="create_time", lookup_expr="gte")

    class Meta:
        model = am.Article
        fields = ["title", "user_id", "status", "game", "article_type", "content", "create_time"]


class PhoneFilter(rf.FilterSet):
    name = rf.CharFilter(field_name="name", lookup_expr="icontains")
    machine_type = rf.ChoiceFilter(choices=am.Phone.PHONE_TYPE)
    brand = rf.ChoiceFilter(choices=am.Phone.PHONE_BRAND)
    version = rf.CharFilter(field_name="version", lookup_expr="icontains")
    net_type = rf.ChoiceFilter(choices=am.Phone.NETWORK)
    screen_size = rf.ChoiceFilter(choices=am.Phone.SCREEN)
    belong_user = rf.CharFilter(field_name="belong_user", lookup_expr="icontains")
    used_user = rf.CharFilter(field_name="used_user", lookup_expr="icontains")
    used_status = rf.ChoiceFilter(choices=am.Phone.USE_STATUS)
    damaged_condition = rf.ChoiceFilter(choices=am.Phone.DAMAGED_STATUS)

    class Meta:
        model = am.Phone
        fields = ["machine_type", "brand", "version", "net_type", "screen_size", "belong_user", "used_status", "damaged_condition"]


class MockServerFilter(rf.FilterSet):
    name = rf.CharFilter(field_name="name", lookup_expr="icontains")
    url_info = rf.CharFilter(field_name="url_info", lookup_expr="icontains")
    request_protocol = rf.ChoiceFilter(choices=am.MockServer.INTERFACE_REQUEST_PROTOCOL)
    request_type = rf.ChoiceFilter(choices=am.MockServer.REQUEST_TYPE)
    timeout = rf.NumberFilter(field_name="timeout", lookup_expr="gte")

    class Meta:
        model = am.MockServer
        fields = ["name", "url_info", "request_protocol", "request_type", "timeout", "return_value"]

