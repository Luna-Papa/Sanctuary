from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class RoleInfo(models.Model):
    role_id = models.CharField(max_length=10, verbose_name='权限编号', primary_key=True)
    role_name = models.CharField(max_length=100, verbose_name='权限名', unique=True)
    role_desc = models.CharField(max_length=100, verbose_name='权限描述')
    role_status = models.BooleanField(verbose_name='有效标识')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='上次修改时间')

    class Meta:
        verbose_name = '权限'
        verbose_name_plural = verbose_name
        ordering = ['role_id']

    def __str__(self):
        return self.role_name


class UserInfo(AbstractUser):
    user_id = models.CharField(max_length=20, verbose_name='用户编号', primary_key=True)
    org_id = models.CharField(max_length=20, verbose_name='所属机构编号')
    username = models.CharField(max_length=100, verbose_name='用户名', unique=True)
    real_name = models.CharField(max_length=50, verbose_name='真实姓名', null=True)
    position = models.CharField(max_length=50, verbose_name='职位', null=True)
    phone = models.CharField(max_length=20, verbose_name='联系方式')
    email = models.EmailField(max_length=100, verbose_name='邮箱', blank=True)

    class Meta:
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name
        ordering = ['user_id']

    def __str__(self):
        return self.username


class UserRole(models.Model):
    user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    role_id = models.ForeignKey(RoleInfo, on_delete=models.CASCADE)
    status = models.BooleanField(verbose_name='有效标识')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='上次修改时间')

    class Meta:
        verbose_name = '用户权限管理'
        verbose_name_plural = verbose_name
        ordering = ['user_id']
        unique_together = ['user_id', 'role_id']

    def __str__(self):
        return self.user_id


class MenuInfo(models.Model):
    CATEGORY_TYPE = (
        (1, "一级菜单"),
        (2, "二级菜单"),
        (3, "三级菜单"),
    )
    menu_id = models.CharField(max_length=10, verbose_name='菜单编号', primary_key=True)
    menu_name = models.CharField(max_length=50, verbose_name='菜单名称', unique=True)
    category_type = models.IntegerField(verbose_name="类目级别", choices=CATEGORY_TYPE, help_text="菜单级别")
    # 设置models有一个指向自己的外键
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True,
                                        verbose_name="父菜单级别",
                                        help_text="父菜单", related_name="sub_cat",
                                        limit_choices_to={'menu_status': True})
    menu_url = models.CharField(max_length=200, verbose_name='菜单访问路径', unique=True)
    menu_desc = models.CharField(max_length=100, verbose_name='描述', blank=True)
    menu_status = models.BooleanField(verbose_name='有效标识')
    menu_show_flag = models.BooleanField(verbose_name='菜单显示标识')
    is_tab = models.BooleanField(verbose_name="是否导航", default=False, help_text="是否导航")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='上次修改时间')

    class Meta:
        verbose_name = '菜单管理'
        verbose_name_plural = verbose_name
        ordering = ['menu_id']

    def __str__(self):
        return self.menu_name


class RoleMenu(models.Model):
    menu_id = models.ForeignKey(MenuInfo, on_delete=models.CASCADE)
    role_id = models.ForeignKey(RoleInfo, on_delete=models.CASCADE)
    status = models.BooleanField(verbose_name='有效标识')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='上次修改时间')

    class Meta:
        verbose_name = '菜单权限管理'
        verbose_name_plural = verbose_name
        ordering = ['menu_id']
        unique_together = ['menu_id', 'role_id']

    def __str__(self):
        return self.menu_id
