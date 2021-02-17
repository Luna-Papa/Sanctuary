from django.urls import path
from dataexp.views import exp_register

urlpatterns = [
    path('exp_register/', exp_register, name='exp_register'),  # 数据提取任务注册
]
