from django_filters import rest_framework as rf
from .models import GameInfo, Channel, ProjectInfo, Task, Article, Phone


class GameInfoFilter(rf.FilterSet):
    game_type = rf.CharFilter(field_name="game_type")
    environment = rf.CharFilter(field_name="environment")
    status = rf.NumberFilter(field_name="status")

    class Meta:
        model = GameInfo
        fields = ["game_type", "environment", "status"]


class ProjectInfoFilter(rf.FilterSet):
    project_name = rf.CharFilter(field_name="project_name")
    responsible_name = rf.CharFilter(field_name="responsible_name")
    status = rf.NumberFilter(field_name="status")

    class Meta:
        model = ProjectInfo
        fields = ["project_name", "responsible_name", "status"]


class TaskFilter(rf.FilterSet):
    name = rf.CharFilter(field_name="name", lookup_expr="icontains")
    task_id = rf.CharFilter(field_name="task_id")
    status = rf.NumberFilter(field_name="status")
    user = rf.CharFilter(field_name="user", lookup_expr="icontains")
    create_time = rf.DateTimeFilter(field_name="create_time", lookup_expr="gte")

    class Meta:
        model = Task
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
        model = Article
        fields = ["title", "user_id", "status", "game", "article_type", "content", "create_time"]


class PhoneFilter(rf.FilterSet):
    name = rf.CharFilter(field_name="name", lookup_expr="icontains")
    machine_type = rf.ChoiceFilter(choices=Phone.PHONE_TYPE)
    brand = rf.ChoiceFilter(choices=Phone.PHONE_BRAND)
    version = rf.CharFilter(field_name="version", lookup_expr="icontains")
    net_type = rf.ChoiceFilter(choices=Phone.NETWORK)
    screen_size = rf.ChoiceFilter(choices=Phone.SCREEN)
    belong_user = rf.CharFilter(field_name="belong_user", lookup_expr="icontains")
    used_user = rf.CharFilter(field_name="used_user", lookup_expr="icontains")
    used_status = rf.ChoiceFilter(choices=Phone.USE_STATUS)
    damaged_condition = rf.ChoiceFilter(choices=Phone.DAMAGED_STATUS)

    class Meta:
        model = Phone
        fields = ["machine_type", "brand", "version", "net_type", "screen_size", "belong_user", "used_status", "damaged_condition"]
