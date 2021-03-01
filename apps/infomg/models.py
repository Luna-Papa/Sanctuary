from django.db import models


# Create your models here.


class SoftwareDefect(models.Model):
    """基础软件缺陷总表"""
    periods = models.CharField(max_length=6, verbose_name='期数')


class DefectDetail(models.Model):
    """缺陷明细记录表"""
    periods = models.CharField(max_length=6, verbose_name='期数')

