from rest_framework.routers import DefaultRouter
from apps.autoAdmin import views
auto_router = DefaultRouter()
auto_router.register(r'game', views.GameInfoViewSet, base_name="game")
auto_router.register(r'project', views.ProjectInfoViewSet, base_name="project")
auto_router.register(r'task', views.TaskViewSet, base_name="task")
auto_router.register(r'article', views.ArticleViewSet, base_name="article")
auto_router.register(r'phone', views.PhoneViewSet, base_name="phone")
auto_router.register(r'interface/info', views.InterfaceInfoViewSet, base_name="interfaceInfo")
