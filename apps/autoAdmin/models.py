from django.db import models
from django.utils import timezone

# Create your models here.


class BaseTable(models.Model):
    create_time = models.DateTimeField('创建时间', default=timezone.now())
    update_time = models.DateTimeField('更新时间', default=timezone.now())

    class Meta:
        abstract = True
        verbose_name = "公共字段表"
        db_table = 'BaseTable'

    def save(self, *args, **kwargs):
        if not self.id:
            self.create_time = timezone.now()
        self.update_time = timezone.now()
        return super(BaseTable, self).save(*args, **kwargs)


class UserType(BaseTable):
    class Meta:
        verbose_name = '用户类型'
        db_table = 'UserType'

    type_name = models.CharField(max_length=20)
    type_desc = models.CharField(max_length=50)


class UserInfo(BaseTable):
    class Meta:
        verbose_name = '用户信息'
        db_table = 'UserInfo'

    username = models.CharField('用户名', max_length=20, unique=True, null=False)
    password = models.CharField('密码', max_length=20, null=False)
    email = models.EmailField('邮箱', null=False, unique=True)
    status = models.IntegerField('有效/无效', default=1)
    # user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)


class ProjectInfo(BaseTable):
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


class ModuleInfo(BaseTable):
    class Meta:
        verbose_name = '模块信息'
        db_table = 'ModuleInfo'

    module_name = models.CharField('模块名称', max_length=50, null=False)
    belong_project = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE)
    test_user = models.CharField('测试负责人', max_length=50, null=False)
    simple_desc = models.CharField('简要描述', max_length=100, null=True)
    other_desc = models.CharField('其他信息', max_length=100, null=True)


class TestCaseInfo(BaseTable):
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


class TestReports(BaseTable):
    class Meta:
        verbose_name = "测试报告"
        db_table = 'TestReports'

    report_name = models.CharField(max_length=40, null=False)
    start_at = models.CharField(max_length=40, null=True)
    status = models.BooleanField()
    testsRun = models.IntegerField()
    successes = models.IntegerField()
    reports = models.TextField()


class EnvInfo(BaseTable):
    class Meta:
        verbose_name = '环境管理'
        db_table = 'EnvInfo'

    env_name = models.CharField(max_length=40, null=False, unique=True)
    base_url = models.CharField(max_length=500, null=False)
    simple_desc = models.CharField(max_length=50, null=False)


# class DebugTalk(BaseTable):
#     belong_project = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE)
#     debugtalk = models.TextField(null=True, default='#debugtalk.py')
#
#     class Meta:
#         verbose_name = '驱动py文件'
#         db_table = 'DebugTalk'


class TestSuite(BaseTable):
    class Meta:
        verbose_name = '用例集合'
        db_table = 'TestSuite'

    belong_project = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE)
    suite_name = models.CharField(max_length=100, null=False)
    include = models.TextField(null=False)


class GameInfo(BaseTable):
    name = models.CharField(max_length=200, null=False)
    game_num = models.IntegerField(help_text='gameId')
    game_type = models.CharField(max_length=20, null=False)
    status = models.IntegerField(help_text='游戏状态')
    environment = models.CharField(max_length=200, null=False)
    memo = models.CharField(max_length=2000, null=True, default='')

    class Meta:
        verbose_name = '渠道表'
        db_table = 'game'


class Channel(BaseTable):
    name = models.CharField(max_length=200, null=False)
    game_num = models.IntegerField(help_text='gameId')
    memo = models.CharField(max_length=2000, null=True, default='')

    class Meta:
        verbose_name = '渠道表'
        db_table = 'channel'


class Task(BaseTable):
    name = models.CharField(max_length=50, null=False)
    task_id = models.CharField(max_length=50, null=False)
    status = models.IntegerField(help_text="0:创建成功，1：构建中，2：被接收，3：运行中，4：已完成，5：丢弃")
    delete_flag = models.IntegerField(default=0, help_text="0:未删除，1:已删除")
    user = models.CharField(max_length=50, help_text="发起人")

    class Meta:
        verbose_name = verbose_name_plural = "任务表"
        db_table = "task"


class Article(BaseTable):
    title = models.CharField(max_length=50, null=False, help_text="文章标题")
    auth = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    content = models.TextField(max_length=5000, null=True, default='', help_text="文章内容")
    game = models.IntegerField(default=0, null=True, help_text="所属游戏ID")
    status = models.IntegerField(default=0, null=True, help_text="0:草稿,1:已发布,2:删除")
    article_type = models.IntegerField(
        default=0,
        help_text=
        "0: 经验杂谈，"
        "1: 项目分享，"
        "2: 注意点相关"
        "3: 流程相关"
        "4: 其它"
    )

    class Meta:
        verbose_name = verbose_name_plural = "文章表"
        db_table = "article"
