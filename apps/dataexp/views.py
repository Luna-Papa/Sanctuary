from django.shortcuts import render
from dataexp.models import SystemInfo, ExpTaskList
# Create your views here.


def exp_register(request):
    systems = SystemInfo.objects.all()
    context = {
        'systems': systems,
        'data_exp_nav_active': True,
    }
    return render(request, 'dataexp/registration.html', context=context)

