from celery import shared_task


@shared_task
def data_push(ds_id, org_no, tb_name, table_id):
    print(ds_id, org_no, tb_name, table_id, 'ok')
