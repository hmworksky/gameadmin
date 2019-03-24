from django_filters import rest_framework as rf
from .models import GameInfo, Channel


class GameInfoFilter(rf.FilterSet):
    game_type = rf.CharFilter(field_name="game_type", lookup_expr="e")
    environment = rf.CharFilter(field_name="environment", lookup_expr="e")
    status = rf.NumberFilter(field_name="status", lookup_expr="e")

    class Meta:
        model = GameInfo
        fields = ["game_type", "environment", "status"]
