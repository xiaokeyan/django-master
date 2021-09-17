import os
import uuid

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from qiniu import Auth, put_file
from rest_framework.response import Response

from tools import _auth_jwt
from .ZXWL_serializers import DynamicDetailSerializer, DynamicClassSerializers
from ZXWL.models import DynamicClass, DynamicDetail
from PayApi.settings import MEDIA_ROOT, Q_N_HTTPS, Q_N_ACCESS_KEY, Q_N_BUCKET_NAME, Q_N_SECRET_KEY


class DynamicClassAdminViewSet(viewsets.ModelViewSet):
    authentication_classes = [_auth_jwt.TokenAuth]
    serializer_class = DynamicClassSerializers
    queryset = DynamicClass.objects.all()


class DynamicClassViewSet(viewsets.ReadOnlyModelViewSet):
    # authentication_classes = [_auth_jwt.TokenAuth]
    serializer_class = DynamicClassSerializers
    queryset = DynamicClass.objects.all()
    # filter_queryset = DynamicClass.objects.all()
    # get_queryset = DynamicClass.objects.all()

    # def create(self, request, *args, **kwargs):
    #     return self.create(self, request, *args, **kwargs)


class DynamicDetailViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DynamicDetailSerializer
    queryset = DynamicDetail.objects.filter(status=True)


class DynamicDetailAdminViewSet(viewsets.ModelViewSet):
    authentication_classes = [_auth_jwt.TokenAuth]
    serializer_class = DynamicDetailSerializer
    queryset = DynamicDetail.objects.filter(status=True)

    def update(self, request, *args, **kwargs):
        request_data = request.data
        pk = request_data.get('id')
        old_obj = DynamicDetail.objects.filter(pk=pk).first()
        dy_ser = self.get_serializer(instance=old_obj, data=request_data, partial=True)
        dy_ser.is_valid(raise_exception=True)
        dy_ser = dy_ser.save()
        return Response({
            'dy_ser': {
                'title': dy_ser.title,
                'content': dy_ser.content,
                'is_hot': dy_ser.is_hot,
                'overview': dy_ser.overview,
                'status': dy_ser.status,
                'dynamic_class_id': dy_ser.dynamic_class_id_id,
                'create_time': dy_ser.create_time,
                'update_time': dy_ser.update_time
            }
        })


class DynamicDetailHotViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DynamicDetailSerializer
    queryset = DynamicDetail.objects.filter(is_hot=True, status=True)[6] if\
        len(DynamicDetail.objects.filter(is_hot=True, status=True)) >= 6\
        else DynamicDetail.objects.filter(is_hot=True, status=True)


# @csrf_exempt
# def upload_imag(request):
#     file_name = ''
#     for i in request.FILES.items():
#         file_name = str(uuid.uuid4()) + i[0]
#         upload_path = os.path.join(MEDIA_ROOT, 'upload')
#         upload_path = os.path.join(upload_path, file_name)
#         with open(upload_path, 'wb') as f:
#             for v in i[1].chunks():
#                 f.write(v)
#     return JsonResponse(
#         {
#             'errno': 0,
#             "data": [
#                 {
#                     'url': 'http://127.0.0.1:8000/media/upload/' + file_name,
#                     'alt': "",
#                     'href': ""
#                 },
#             ]
#         }
#     )


@csrf_exempt
def upload_imag(request):
    for file in request.FILES.items():
        file_name = str(uuid.uuid4()) + file[0]
        upload_path = os.path.join(MEDIA_ROOT, 'upload//')
        upload_file_path = os.path.join(upload_path, file_name)
        with open(upload_file_path, 'wb') as f:
            for v in file[1].chunks():
                f.write(v)
        file_path = upload_path + file_name
        access_key = Q_N_ACCESS_KEY
        secret_key = Q_N_SECRET_KEY
        bucket_name = Q_N_BUCKET_NAME
        q = Auth(access_key, secret_key)
        # 获取七牛云token
        token = q.upload_token(bucket=bucket_name)
        # 获取绝对路径
        ret, info = put_file(token, file_name, file_path, version='v2')
        return JsonResponse(
            {
                'errno': 0,
                "data": [
                    {
                        'url': Q_N_HTTPS + ret['key'],
                        'alt': "",
                        'href': ""
                    },
                ]
            }
        )
