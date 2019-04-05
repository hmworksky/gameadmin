from django_filters import rest_framework as rf
from .models import GameInfo, Channel, ProjectInfo, Task, Article


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
    name = rf.CharFilter(field_name="name")
    task_id = rf.CharFilter(field_name="task_id")
    status = rf.NumberFilter(field_name="status")
    user = rf.CharFilter(field_name="user")
    raw_add_time = rf.DateTimeFilter(field_name="raw_add_time")

    class Meta:
        model = Task
        fields = ["name", "task_id", "status", "user", "raw_add_time"]
