from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.generic import View
from sjxf.models import DataSub, DataUsers, BaseTables, TaskExecuteQueen, DataRelation
from sjxf.tasks import data_push
import json


# Create your views here.


class BaseTablesView(View):
    """下发表列表"""

    def get(self, request):
        all_tables = BaseTables.objects.filter(flag=0)
        return render(request, 'sjxf/basetables.html',
                      {'all_tables': all_tables, 'sjxf_nav_active': True})


class ManualSjxf(View):
    def get(self, request):
        users = list(DataUsers.objects.all().values('user_id', 'org_name'))
        tables = list(BaseTables.objects.filter(flag=0).values('id', 'ds_id', 'table_name'))
        context = {
            'data_users': users,
            'tables': tables,
            'sjxf_nav_active': True,
        }
        return render(request, 'sjxf/manualSJXF.html', context=context)

    def post(self, request):
        org_no = request.POST.get('org_no')
        table_id = request.POST.get('table_id')
        # 取出后台全量数据下发任务所需参数值
        #     1 渠道名称：  DS_ID
        #     2 机构  号：  DUSER_ID
        #     3 数据表名：  TBNAME
        #     4 数据表ID:   T_ID
        queryset = BaseTables.objects.get(id=table_id)
        ds_id = queryset.ds_id
        tb_name = queryset.table_name
        # 调用celery异步任务
        data_push.delay(ds_id, org_no, tb_name, table_id)
        return HttpResponse('add task success.')


class DataRelationView(View):
    def get(self, request):
        return render(request, 'sjxf/datarelations.html', {'sjxf_nav_active': True})


def ajax_data_relations(request):
    relation_list = []
    if request.method == 'POST':
        org_no = request.POST.get('org_no')
        table_name = request.POST.get('table_name')
        if org_no:
            relations = DataRelation.objects.filter(user_id=org_no)  # 按机构号精准匹配
        elif table_name:
            if len(table_name.strip()) >= 4:
                relations = DataRelation.objects.filter(table_name__icontains=table_name)
            else:
                relations = []
        else:
            relations = DataRelation.objects.all()[:200]
        for relation_info in relations:
            relation_list.append({
                'user_id': relation_info.user_id,
                'org_name': relation_info.org_name,
                'ds_id': relation_info.ds_id,
                'table_name': relation_info.table_name,
                'c_user_id': relation_info.c_user_id,
                'create_date': relation_info.create_date.strftime('%Y-%m-%d %H:%M:%S'),
            })
        return HttpResponse(json.dumps(relation_list), content_type="application/json")
