from django.shortcuts import render
from django.views.generic import View
from sjxf.models import DataSub, DataUsers, BaseTables, TaskExecuteQueen, DataRelation
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
        tables = list(BaseTables.objects.all().values('table_name'))
        context = {
            'data_users': users,
            'tables': tables,
        }
        return render(request, 'sjxf/manualSJXF.html', context=context)


class DataRelationView(View):
    def get(self, request):
        relations = list(DataRelation.objects.all().
                         values('user_id', 'org_name', 'ds_id', 'table_name', 'c_user_id', 'create_date'))
        return render(request, 'sjxf/datarelations.html', {'relations': relations})
