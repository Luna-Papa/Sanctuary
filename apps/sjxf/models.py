from django.db import models
from users.models import UserInfo
# Create your models here.


class StatusTypes(models.TextChoices):
    """任务状态类型定义"""
    status_waiting = '0', '未执行'
    status_begin = '1', '执行开始'
    status_success = '2', '执行完成'
    status_failed = '3', '执行失败'


class BaseTables(models.Model):
    """ 数据下发基础表定义"""
    id = models.CharField(verbose_name='序号', max_length=10, primary_key=True)
    creator = models.CharField(verbose_name='模式名', max_length=50)
    table_name = models.CharField(verbose_name='下发表名', max_length=100)
    ds_id = models.CharField(verbose_name='渠道名', max_length=10)
    flag = models.BooleanField(verbose_name='是否生效')
    chn_name = models.CharField(verbose_name='表中文名', max_length=100)
    create_date = models.DateTimeField(verbose_name='创建日期')

    class Meta:
        verbose_name = '数据下发基础表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.table_name


class DataUsers(models.Model):
    """数据下发用户"""
    user_id = models.CharField(verbose_name='用户编号', max_length=10, primary_key=True)
    org_name = models.CharField(verbose_name='机构名称', max_length=100)
    ip_addr = models.GenericIPAddressField(verbose_name='IP地址')
    port = models.IntegerField(verbose_name='端口')
    # username = models.CharField(verbose_name='服务器用户名', max_length=50, null=True)
    # password = models.CharField(verbose_name='服务器用户密码', max_length=50, null=True)
    # save_path = models.CharField(verbose_name='保存路径', max_length=500, null=True)
    # deliveryer = models.CharField(verbose_name='代号', max_length=50, default='D01')
    flag = models.BooleanField(verbose_name='激活标识')
    user_no = models.CharField(verbose_name='用户编号', max_length=10, null=True)
    pass_no = models.CharField(verbose_name='文件密码', max_length=10, null=True)

    class Meta:
        verbose_name = '数据下发用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_id


class DataSub(models.Model):
    """数据下发任务"""
    id = models.BigIntegerField(verbose_name='序号', primary_key=True)
    user_id = models.CharField(verbose_name='机构编号', max_length=10, db_index=True)
    ds_id = models.CharField(verbose_name='渠道编号', max_length=10)
    ds_type = models.IntegerField(verbose_name='类型')
    t_id = models.CharField(max_length=50, verbose_name='数据表名')
    seq = models.IntegerField(verbose_name='顺序号')
    file_type = models.CharField(max_length=10, verbose_name='文件类型')
    modified = models.CharField(verbose_name='导出限定', max_length=150)
    h_sql = models.CharField(verbose_name='导出语句', max_length=2000)
    h_where = models.CharField(verbose_name='查询条件', max_length=500)
    c_user_id = models.CharField(verbose_name='村镇银行编号', max_length=10)
    a_where = models.CharField(verbose_name='全量查询条件', max_length=500)
    create_date = models.DateTimeField(verbose_name='创建日期')

    class Meta:
        verbose_name = '数据下发任务'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_id


class DataRelation(models.Model):
    id = models.BigIntegerField(verbose_name='序号', primary_key=True)
    user_id = models.CharField(verbose_name='机构编号', max_length=10, db_index=True)
    org_name = models.CharField(verbose_name='机构名称', max_length=100)
    ds_id = models.CharField(verbose_name='渠道编号', max_length=10)
    table_name = models.CharField(verbose_name='下发表名', max_length=100)
    c_user_id = models.CharField(verbose_name='村镇银行编号', max_length=10)
    create_date = models.DateTimeField(verbose_name='创建日期', null=True)

    class Meta:
        verbose_name = '数据下发关系'
        verbose_name_plural = verbose_name
        ordering = ['user_id', 'ds_id']

    def __str__(self):
        return self.user_id


class TaskExecuteQueen(models.Model):
    task_id = models.AutoField(verbose_name='任务编号', primary_key=True)
    task_name = models.CharField(verbose_name='任务名称', max_length=200)
    user_id = models.ForeignKey(UserInfo, verbose_name='任务发起人id', on_delete=models.DO_NOTHING)
    user_name = models.CharField(verbose_name='任务发起人姓名', max_length=100)
    org_id = models.CharField(max_length=20, verbose_name='所属机构编号')
    create_date = models.DateTimeField(verbose_name='任务创建日期')
    end_date = models.DateTimeField(verbose_name='任务结束日期', null=True)
    status = models.CharField(verbose_name='执行状态', choices=StatusTypes.choices, max_length=1)
    content = models.TextField(verbose_name='任务执行日志', null=True)

    class Meta:
        verbose_name = '任务执行队列'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.task_name

