from django.urls import path
from apps.sjxf.views import BaseTablesView, ManualSjxf, DataRelationView


urlpatterns = [
    path('basetables/', BaseTablesView.as_view(), name='get_base_table'),
    path('manual-sjxf/', ManualSjxf.as_view(), name='manual_sjxf'),
    path('datasubs/', DataRelationView.as_view(), name='get_data_relation'),
]
