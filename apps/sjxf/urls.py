from django.urls import path
from apps.sjxf.views import BaseTablesView, ManualSjxf, DataRelationView, ajax_data_relations


urlpatterns = [
    path('basetables/', BaseTablesView.as_view(), name='get_base_table'),
    path('manual-sjxf/', ManualSjxf.as_view(), name='manual_sjxf'),
    path('datasubs/', DataRelationView.as_view(), name='get_data_relation'),
    path('get_data_relations/', ajax_data_relations, name='filter_data_relation'),
]
