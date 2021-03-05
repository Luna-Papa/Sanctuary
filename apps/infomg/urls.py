from django.urls import path
from infomg.views import defect_import, defect_list, defect_detail


app_name = 'InfoMG'
urlpatterns = [
    path('defect_import/', defect_import, name='defect_imp'),  # 基础软硬件缺陷导入
    path('defect_list/', defect_list, name='defect_list'),  # 基础软硬件缺陷查看
    path('defect_detail/', defect_detail, name='defect_detail'),  # 缺陷明细查看
]
