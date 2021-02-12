from django.shortcuts import render
from django.views.generic import View
from sjxf.models import DataSub, DataUsers, BaseTables, TaskExecuteQueen
from django.http import JsonResponse


# Create your views here.


class BaseTablesView(View):
    """下发表列表"""
    def get(self, request):
        all_tables = BaseTables.objects.all()
        return render(request, 'sjxf/basetables.html', {'all_tables': all_tables})


class ManualSjxf(View):
    def get(self, request):
        users = list(DataUsers.objects.all().values('user_id', 'org_name'))
        return render(request, 'sjxf/manualSJXF.html', {'data_users': users})


def get_data_user(request):
    if request.method == 'GET':
        users = list(DataUsers.objects.all().values('user_id', 'org_name'))
        return JsonResponse(users, safe=False)
