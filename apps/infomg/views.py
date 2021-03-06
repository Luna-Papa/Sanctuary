from django.shortcuts import render
from infomg.models import ProductDefect
from django.db import transaction
import xlrd
from xlrd import xldate_as_tuple
from datetime import datetime


# Create your views here.


def defect_import(request):
    if request.method == 'GET':
        return render(request, 'infomg/defect_imp.html')
    elif request.method == 'POST':
        f = request.FILES.get('file')
        periods = request.POST.get('periods')
        excel_type = f.name.split('.')[-1]
        if excel_type in ['xls', 'xlsx']:
            wb = xlrd.open_workbook(filename=None, file_contents=f.read())
            table = wb.sheets()[0]
            rows = table.nrows
            try:
                with transaction.atomic():
                    for i in range(3, rows):
                        i_row = table.row_values(i)
                        try:
                            number = int(i_row[0])
                        except Exception as e:
                            break
                        category = i_row[1]
                        model = i_row[2]
                        manufacturer = i_row[3]
                        reason = i_row[4]
                        defect = i_row[5]
                        solution = i_row[6]
                        fix_pack = i_row[7]
                        status = i_row[8]
                        find_date = datetime(*xldate_as_tuple(i_row[9], 0))
                        task = ProductDefect(periods=periods, number=number, category=category,
                                             model=model, manufacturer=manufacturer, reason=reason,
                                             defect=defect, solution=solution, fix_pack=fix_pack,
                                             status=status, find_date=find_date)
                        task.save()
                all_defects = ProductDefect.objects.filter(periods=periods).values()
                return render(request, "infomg/defect_list.html", {'all_defects': all_defects, 'periods': periods})
            except Exception as e:
                print(e)


def defect_list(request):
    if request.method == 'GET':
        all_defects = ProductDefect.objects.all().values()

        return render(request, 'infomg/defect_list.html', {'all_defects': all_defects})


def defect_detail(request):
    return render(request, 'infomg/defect_detail.html')


def add_defect_detail(request, defect_id=None):
    if request.method == 'GET':
        if defect_id:
            defects = ProductDefect.objects.get(pk=defect_id).values()
            return render(request, 'infomg/add_defect_detail.html', {'defects': defects})
        else:
            defects = ProductDefect.objects.all().values()
            periods = ProductDefect.objects.all().values('periods').distinct()
            return render(request, 'infomg/add_defect_detail.html', {'defects': defects, 'periods': periods})
