from django.core.paginator import Paginator


def PostData(data, db_serializer, put_obj = None):
    status = 200
    try:
        if put_obj:
            serial_data = db_serializer(put_obj,data=data)
        else:
            serial_data = db_serializer(data=data)
        if serial_data.is_valid():
            serial_data.save()
            status = 200
            serial_data = serial_data.data
        else:
            serial_data = serial_data.errors

    except Exception as e:
        print(e)
        serial_data = [e]
        status = 204
    return serial_data, status


def GetData(kwargs, db_model, db_serializer, serialized_output=True, pages=None, search_param=None):
    status = 200
    serial_data = ()
    data = list()
    if kwargs:
        search_param = kwargs
        pages = None

    try:
        if search_param or kwargs:
            data = db_model.objects.filter(**search_param)
        else:
            data = db_model.objects.all()

        data = get_pagination(data, pages)
        serial_data = (db_serializer(data, many=True)).data
        if not serial_data:
            status = 204

    except Exception as e:
        print(e)
        status = 204

    if not serialized_output:
        return data,status

    return serial_data, status


def get_pagination(data, pages):
    if pages and 'per_page' in pages:
        data = get_pagination(data, pages)
        page_obj = Paginator(data, pages['per_page'])
        data = page_obj.page(1 if not 'page' in pages else pages['page'])
    return data
