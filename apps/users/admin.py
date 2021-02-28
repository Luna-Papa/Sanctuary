from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from django.utils.translation import gettext_lazy
from users.models import UserInfo, Slogan
# Register your models here.


admin.site.site_header = '驾驶舱管理后台'
admin.site.site_title = '驾驶舱'


@admin.register(UserInfo)
class UserInfoAdmin(UserAdmin):
    list_display = ('username', 'org_id', 'real_name', 'department', 'position', 'phone')
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        ('用户信息', {'fields': ('org_id', 'real_name', 'position', 'phone', 'email')}),
        ('角色信息', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('权限管理', {'fields': ('roles',)}),
        ('其它信息', {'fields': ('last_login', 'date_joined')}),
    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('用户信息', {'fields': ('org_id', 'real_name', 'department', 'position', 'phone', 'email')}),
        ('角色信息', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('权限管理', {'fields': ('roles',)}),
        ('其它信息', {'fields': ('last_login', 'date_joined')}),
    )
    search_fields = ['username', 'org_id', 'real_name', 'phone']
    filter_horizontal = ('roles',)


# @admin.register(RoleInfo)
# class RoleInfoAdmin(admin.ModelAdmin):
#     list_display = ('role_name', 'role_desc', 'role_status', 'created_time', 'updated_time')
#     fields = ('role_name', 'role_desc', 'role_status')
#     search_fields = ['role_name', 'role_desc']
