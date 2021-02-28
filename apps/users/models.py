from django.db import models
from django.contrib.auth.models import AbstractUser
from rbac.models import Role


# Create your models here.

# class RoleInfo(models.Model):
#     role_name = models.CharField(max_length=100, verbose_name='权限名', unique=True)
#     url_name = models.CharField(max_length=200, verbose_name='URL配置项名称')
#     role_desc = models.CharField(max_length=100, verbose_name='权限描述')
#     role_status = models.BooleanField(verbose_name='有效标识')
#     created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
#     updated_time = models.DateTimeField(auto_now=True, verbose_name='上次修改时间')
#
#     class Meta:
#         verbose_name = '权限管理'
#         verbose_name_plural = verbose_name
#         ordering = ['role_name']
#
#     def __str__(self):
#         return self.role_name


class UserInfo(AbstractUser):
    org_id = models.CharField(max_length=20, verbose_name='所属机构编号', null=True)
    real_name = models.CharField(max_length=50, verbose_name='真实姓名', null=True)
    department = models.CharField(max_length=100, verbose_name='部门', null=True)
    position = models.CharField(max_length=50, verbose_name='职位', null=True)
    phone = models.CharField(max_length=20, verbose_name='联系方式', null=True)
    email = models.EmailField(max_length=100, verbose_name='邮箱', blank=True)
    roles = models.ManyToManyField(verbose_name='拥有角色', to=Role, blank=True)

    class Meta:
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name
        ordering = ['username']

    def __str__(self):
        return self.username


# class UserRole(models.Model):
#     username = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name='用户名')
#     role_name = models.ForeignKey(RoleInfo, on_delete=models.CASCADE)
#     status = models.BooleanField(verbose_name='有效标识')
#     created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
#     updated_time = models.DateTimeField(auto_now=True, verbose_name='上次修改时间')
#
#     class Meta:
#         verbose_name = '用户权限管理'
#         verbose_name_plural = verbose_name
#         ordering = ['username']
#         unique_together = ['username', 'role_name']
#
#     def __str__(self):
#         return self.username
#
#
# class MenuInfo(models.Model):
#     CATEGORY_TYPE = (
#         (1, "一级菜单"),
#         (2, "二级菜单"),
#         (3, "三级菜单"),
#     )
#     menu_id = models.CharField(max_length=10, verbose_name='菜单编号', primary_key=True)
#     menu_name = models.CharField(max_length=50, verbose_name='菜单名称', unique=True)
#     category_type = models.IntegerField(verbose_name="类目级别", choices=CATEGORY_TYPE, help_text="菜单级别")
#     # 设置models有一个指向自己的外键
#     parent_category = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True,
#                                         verbose_name="父菜单级别",
#                                         help_text="父菜单", related_name="sub_cat",
#                                         limit_choices_to={'menu_status': True})
#     menu_url = models.CharField(max_length=200, verbose_name='菜单访问路径', unique=True)
#     menu_desc = models.CharField(max_length=100, verbose_name='描述', blank=True)
#     menu_status = models.BooleanField(verbose_name='有效标识')
#     menu_show_flag = models.BooleanField(verbose_name='菜单显示标识')
#     is_tab = models.BooleanField(verbose_name="是否导航", default=False, help_text="是否导航")
#     created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
#     updated_time = models.DateTimeField(auto_now=True, verbose_name='上次修改时间')
#
#     class Meta:
#         verbose_name = '菜单管理'
#         verbose_name_plural = verbose_name
#         ordering = ['menu_id']
#
#     def __str__(self):
#         return self.menu_name
#
#
# class RoleMenu(models.Model):
#     menu_id = models.ForeignKey(MenuInfo, on_delete=models.CASCADE)
#     role_name = models.ForeignKey(RoleInfo, on_delete=models.CASCADE)
#     status = models.BooleanField(verbose_name='有效标识')
#     created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
#     updated_time = models.DateTimeField(auto_now=True, verbose_name='上次修改时间')
#
#     class Meta:
#         verbose_name = '菜单权限管理'
#         verbose_name_plural = verbose_name
#         ordering = ['menu_id']
#         unique_together = ['menu_id', 'role_name']
#
#     def __str__(self):
#         return self.menu_id
#
#
class Slogan(models.Model):
    text = models.CharField(verbose_name='标语', max_length=200, unique=True)
    v_flag = models.BooleanField(verbose_name='有效标识')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='上次修改时间')

    class Meta:
        verbose_name = '标语管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text

# class Organization(models.Model):
#     org_id = models.CharField(max_length=20, verbose_name='机构编号', primary_key=True)
#     org_name = models.CharField(max_length=100, verbose_name='机构名称')
#
#     def __str__(self):
#         return self.org_id
#
#     class Meta:
#         verbose_name = '机构信息'
#         verbose_name_plural = verbose_name
