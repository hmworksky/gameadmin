from django.db import models
from django.utils import timezone

# Create your models here.


# class BaseTable(models.Model):
#     create_time = models.DateTimeField('创建时间', default=timezone.now())
#     update_time = models.DateTimeField('更新时间', default=timezone.now())
#
#     class Meta:
#         abstract = True
#         verbose_name = "公共字段表"
#         db_table = 'models.Model'
#
#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.create_time = timezone.now()
#         self.update_time = timezone.now()
#         return super(models.Model, self).save(*args, **kwargs)


class UserType(models.Model):
    class Meta:
        verbose_name = '用户类型'
        db_table = 'UserType'

    type_name = models.CharField(max_length=20)
    type_desc = models.CharField(max_length=50)


class UserInfo(models.Model):
    class Meta:
        verbose_name = '用户信息'
        db_table = 'UserInfo'

    username = models.CharField('用户名', max_length=20, unique=True, null=False)
    password = models.CharField('密码', max_length=20, null=False)
    email = models.EmailField('邮箱', null=False, unique=True)
    status = models.IntegerField('有效/无效', default=1)
    # user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)


class ProjectInfo(models.Model):
    class Meta:
        verbose_name = '项目信息'
        db_table = 'ProjectInfo'

    project_name = models.CharField('项目名称', max_length=50, unique=True, null=False)
    responsible_name = models.CharField('负责人', max_length=20, null=False)
    test_user = models.CharField('测试人员', max_length=100, null=False)
    dev_user = models.CharField('开发人员', max_length=100, null=False)
    publish_app = models.CharField('发布应用', max_length=100, null=False)
    status = models.IntegerField(default=0, help_text=
                                 "项目状态：0:PRD，1:DEV，2:TEST,3:PRE,4:PUBLISHED"
                                 )
    simple_desc = models.CharField('简要描述', max_length=100, null=True)
    other_desc = models.CharField('其他信息', max_length=100, null=True)


class ModuleInfo(models.Model):
    class Meta:
        verbose_name = '模块信息'
        db_table = 'ModuleInfo'

    module_name = models.CharField('模块名称', max_length=50, null=False)
    belong_project = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE)
    test_user = models.CharField('测试负责人', max_length=50, null=False)
    simple_desc = models.CharField('简要描述', max_length=100, null=True)
    other_desc = models.CharField('其他信息', max_length=100, null=True)


class TestCaseInfo(models.Model):
    class Meta:
        verbose_name = '用例信息'
        db_table = 'TestCaseInfo'

    type = models.IntegerField('test/config', default=1)
    name = models.CharField('用例/配置名称', max_length=50, null=False)
    belong_project = models.CharField('所属项目', max_length=50, null=False)
    belong_module = models.ForeignKey(ModuleInfo, on_delete=models.CASCADE)
    include = models.CharField('前置config/test', max_length=1024, null=True)
    author = models.CharField('编写人员', max_length=20, null=False)
    request = models.TextField('请求信息', null=False)


class TestReports(models.Model):
    class Meta:
        verbose_name = "测试报告"
        db_table = 'TestReports'

    report_name = models.CharField(max_length=40, null=False)
    start_at = models.CharField(max_length=40, null=True)
    status = models.BooleanField()
    testsRun = models.IntegerField()
    successes = models.IntegerField()
    reports = models.TextField()


class EnvInfo(models.Model):
    class Meta:
        verbose_name = '环境管理'
        db_table = 'EnvInfo'

    env_name = models.CharField(max_length=40, null=False, unique=True)
    base_url = models.CharField(max_length=500, null=False)
    simple_desc = models.CharField(max_length=50, null=False)


# class DebugTalk(models.Model):
#     belong_project = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE)
#     debugtalk = models.TextField(null=True, default='#debugtalk.py')
#
#     class Meta:
#         verbose_name = '驱动py文件'
#         db_table = 'DebugTalk'


class TestSuite(models.Model):
    class Meta:
        verbose_name = '用例集合'
        db_table = 'TestSuite'

    belong_project = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE)
    suite_name = models.CharField(max_length=100, null=False)
    include = models.TextField(null=False)


class GameInfo(models.Model):
    GAME_STATUS = (
        (0, 'prd'),
        (1, 'dev'),
        (2, 'test'),
        (3, 'pre'),
        (4, 'published'),
    )
    GAME_ENV = (
        ('dev', '开发环境'),
        ('test', '测试环境'),
        ('prd', '生产环境')
    )
    GAME_TYPE = (
        (0, '人人游戏'),
        (1, '人机游戏'),
        (2, '角色扮演'),
        (3, '平台'),
        (4, '房卡游戏'),
    )
    name = models.CharField("游戏名称", max_length=200, null=False)
    game_num = models.IntegerField('gameId')
    game_type = models.IntegerField("游戏类型", default=0, choices=GAME_TYPE)
    status = models.IntegerField('游戏状态', default=0, choices=GAME_STATUS)
    env = models.CharField("当前环境", max_length=200, default="dev", null=False, choices=GAME_ENV)
    memo = models.TextField("描述", max_length=2000, null=True, default='')

    class Meta:
        verbose_name = '游戏信息表'
        db_table = 'game'


class Channel(models.Model):
    name = models.CharField(max_length=200, null=False)
    game_num = models.IntegerField(help_text='gameId')
    memo = models.CharField(max_length=2000, null=True, default='')

    class Meta:
        verbose_name = '渠道表'
        db_table = 'channel'


class Task(models.Model):
    STATUS_LIST = (
        (0, "创建成功"),
        (1, "构建中"),
        (2, "被接收"),
        (3, "运行中"),
        (4, "已完成"),
        (5, "丢弃"),
    )
    name = models.CharField(max_length=50, null=False)
    task_id = models.CharField(max_length=50, null=False)
    status = models.IntegerField(default=0, choices=STATUS_LIST, help_text="0:创建成功，1：构建中，2：被接收，3：运行中，4：已完成，5：丢弃")
    delete_flag = models.IntegerField(default=0, help_text="0:未删除，1:已删除")
    user = models.CharField(max_length=50, help_text="发起人")

    class Meta:
        verbose_name = verbose_name_plural = "任务表"
        db_table = "task"


class Article(models.Model):
    title = models.CharField(max_length=50, null=False, help_text="文章标题")
    user_id = models.IntegerField(default=0, null=False, help_text="用户ID")
    content = models.TextField(max_length=5000, null=True, default='', help_text="文章内容")
    game = models.IntegerField(default=0, null=True, help_text="所属游戏ID")
    status = models.IntegerField(default=0, null=True, help_text="0:草稿,1:已发布,2:删除")
    article_type = models.IntegerField(
        default=0,
        help_text="""
        0: 经验杂谈，
        1: 项目分享，
        2: 注意点相关
        3: 流程相关
        4: 其它
        """
    )

    class Meta:
        verbose_name = verbose_name_plural = "文章表"
        db_table = "article"


class Phone(models.Model):
    PHONE_TYPE = (
        (0, '苹果'),
        (1, '安卓')
    )
    PHONE_BRAND = (
        (0, '苹果'),
        (1, '三星'),
        (2, '荣耀'),
        (3, '魅族'),
        (4, '华为'),
        (5, '诺基亚'),
        (6, 'OPPO'),
        (7, 'VIVO'),
    )
    NETWORK = (
        (0, '移动'),
        (1, '联通'),
        (2, '电信'),
        (3, '其它'),
    )
    SCREEN = (
        (0, '4.5寸以下'),
        (1, '4.5-5.0寸'),
        (2, '5.0-5.5寸'),
        (3, '5.5寸以上'),
    )
    USE_STATUS = (
        (0, '未使用'),
        (1, '使用中'),
        (2, '借出'),
    )
    DAMAGED_STATUS = (
        (0, '正常'),
        (1, '损坏')
    )
    name = models.CharField(max_length=50, null=False, help_text="手机名字")
    machine_type = models.IntegerField(default=0, choices=PHONE_TYPE, help_text="手机类型")
    brand = models.IntegerField(default=0, choices=PHONE_BRAND, help_text="厂家")
    version = models.CharField(max_length=50, null=False, help_text="系统版本")
    net_type = models.IntegerField(default=0, choices=NETWORK, help_text="运营商")
    screen_size = models.IntegerField(default=0, choices=SCREEN, help_text="屏幕大小")
    belong_user = models.CharField(max_length=20, default='', null=True, help_text="所属人")
    used_user = models.CharField(max_length=20, default='', null=True, help_text="使用人")
    used_status = models.IntegerField(default=1, choices=USE_STATUS, help_text="使用状态")
    damaged_condition = models.IntegerField(default=0, choices=DAMAGED_STATUS, help_text="损坏状态")

    class Meta:
        verbose_name = verbose_name_plural = "手机信息表"
        db_table = "phone"


class InterfaceInfo(models.Model):
    """接口信息表"""

    INTERFACE_REQUEST_PROTOCOL = (
        (0, "http"),
        (1, "primus"),
        (2, "socketIO"),
        (3, "rpc"),
        (4, "dubbo")
    )
    INTERFACE_REQUEST_METHOD = (
        (0, ""),
        (1, "post"),
        (2, "delete"),
        (3, "put"),
        (4, "patch"),
        (5, "get"),
    )
    INTERFACE_APP = (
        (0, "wap"),
        (1, "admin"),
        (2, "node"),
        (3, "java")
    )
    name = models.CharField(max_length=50,  null=False, help_text="接口名")
    path = models.CharField(max_length=50,  null=False, help_text="接口路径")
    request_protocol = models.IntegerField(default=0, choices=INTERFACE_REQUEST_PROTOCOL, help_text="请求协议")
    request_method = models.IntegerField(default=0, null=True, choices=INTERFACE_REQUEST_METHOD, help_text="请求方式")
    route = models.CharField(default="router", max_length=50, null=True, help_text="socketIO绑定路由，一般为router")
    project = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE, help_text="项目ID")
    app_name = models.IntegerField(default=0, choices=INTERFACE_APP, help_text="应用名")

    class Meta:
        verbose_name = verbose_name_plural = "接口信息表"
        db_table = "interface_info"
        unique_together = ("name", "path", "project")


class InterfaceField(models.Model):
    """接口字段表"""
    INTERFACE_GENRE = (
        (0, "string"),
        (1, "int"),
        (2, "float"),
        (3, "bool"),
        (4, "double"),
    )
    name = models.CharField(max_length=50, null=False, help_text="字段名")
    genre = models.IntegerField(default=0, choices=INTERFACE_GENRE, help_text="接口类型")
    length = models.IntegerField(default=1, help_text="字段长度")
    interface = models.ForeignKey(InterfaceInfo, on_delete=models.CASCADE, help_text="接口ID")

    class Meta:
        verbose_name = verbose_name_plural = "接口字段表"
        db_table = "interface_field"
        unique_together = ("name", "interface")


class MockServer(models.Model):

    INTERFACE_REQUEST_PROTOCOL = (
        (0, "HTTP"),
        (1, "PRIMUS"),
        (2, "socketIO"),
        (3, "RPC"),
        (4, "dubbo")
    )
    REQUEST_TYPE = (
        (1, "忽略原请求"),
        (2, "返回指定值"),
        (3, "请求JAVA返回JAVA结果"),
        (4, "继续请求JAVA返回指定结果"),
    )
    name = models.CharField(max_length=50, null=False, help_text="MockServer名字")
    url_info = models.URLField(max_length=500, null=False, help_text="接口path")
    request_protocol = models.IntegerField(default=0, null=True, choices=INTERFACE_REQUEST_PROTOCOL, help_text="请求协议")
    request_type = models.IntegerField(default=1, null=True, choices=REQUEST_TYPE, help_text="请求类型")
    return_value = models.TextField(default='', null=True, max_length=1000)
    timeout = models.IntegerField(default=0, null=False, help_text="超时时间")

    class Meta:
        verbose_name = verbose_name_plural = "mock_server"
        db_table = "mock_server"
        unique_together = ("name", "url_info")
