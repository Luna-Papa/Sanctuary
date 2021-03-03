from django.conf import settings
from rbac.models import Permission

"""
该函数在用户登录后调用，根据用户权限进行数据初始化，写入session中。
"""


def init_permission(request, user_obj):
    if user_obj.is_superuser:
        permission_item_list = Permission.objects.all().values(
            'id',
            'title',
            'url',
            'perm_code',
            'pid_id',
            'perm_group_id',
            'perm_group__menu_id',
            'perm_group__menu__title',
            'perm_group__menu__icon',
        ).distinct()
        permission_url_list = {}
        permission_menu_list = []
        for item in permission_item_list:
            perm_group_id = item['perm_group_id']
            url = item['url']
            perm_code = item['perm_code']
            if perm_group_id in permission_url_list:
                permission_url_list[perm_group_id]['codes'].append(perm_code)
                permission_url_list[perm_group_id]['urls'].append(url)
            else:
                permission_url_list[perm_group_id] = {'codes': [perm_code, ], 'urls': [url, ]}
        request.session[settings.PERMISSION_URL_KEY] = permission_url_list

        for item in permission_item_list:
            tpl = {
                'id': item['id'],
                'title': item['title'],
                'url': item['url'],
                'pid_id': item['pid_id'],
                'menu_id': item['perm_group__menu_id'],
                'menu_title': item['perm_group__menu__title'],
                'menu_icon': item['perm_group__menu__icon'],
            }
            permission_menu_list.append(tpl)
        request.session[settings.PERMISSION_MENU_KEY] = permission_menu_list

    else:
        permission_item_list = user_obj.roles.values('permissions__id',
                                                     'permissions__title',
                                                     'permissions__url',
                                                     'permissions__perm_code',
                                                     'permissions__pid_id',
                                                     'permissions__perm_group_id',
                                                     'permissions__perm_group__menu_id',
                                                     'permissions__perm_group__menu__title',
                                                     'permissions__perm_group__menu__icon',
                                                     ).distinct()

        permission_url_list = {}
        permission_menu_list = []

        for item in permission_item_list:
            perm_group_id = item['permissions__perm_group_id']
            url = item['permissions__url']
            perm_code = item['permissions__perm_code']
            if perm_group_id in permission_url_list:
                permission_url_list[perm_group_id]['codes'].append(perm_code)
                permission_url_list[perm_group_id]['urls'].append(url)
            else:
                permission_url_list[perm_group_id] = {'codes': [perm_code, ], 'urls': [url, ]}
        request.session[settings.PERMISSION_URL_KEY] = permission_url_list

        for item in permission_item_list:
            tpl = {
                'id': item['permissions__id'],
                'title': item['permissions__title'],
                'url': item['permissions__url'],
                'pid_id': item['permissions__pid_id'],
                'menu_id': item['permissions__perm_group__menu_id'],
                'menu_title': item['permissions__perm_group__menu__title'],
                'menu_icon': item['permissions__perm_group__menu__icon'],
            }
            permission_menu_list.append(tpl)
        request.session[settings.PERMISSION_MENU_KEY] = permission_menu_list
