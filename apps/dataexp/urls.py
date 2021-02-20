from django.urls import path
from dataexp.views import exp_register, download_template

urlpatterns = [
    path('exp_register/', exp_register, name='exp_register'),  # 数据提取任务注册
    path('download_template/', download_template, name='download_template'),  # 下载数据提取登记模板
]
