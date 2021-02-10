from django.shortcuts import render
from django.views.generic import View
from sjxf.models import DataSub, DataUsers, BaseTables, TaskExecuteQueen


# Create your views here.


class BaseTablesView(View):
    """下发表列表"""
    def get(self, request):
        all_tables = BaseTables.objects.all()
        return render(request, 'sjxf/basetables.html', {'all_tables': all_tables})


def single_table_push(request, table_name, org_no):
    """登记单表单机构下发任务"""
    pass
