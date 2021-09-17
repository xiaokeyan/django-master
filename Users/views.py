from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer

from .models import Users, WorkerUser
from .Users_serializers import UsersAuthSerializers, UsersAuthDetailSerializer,\
    WorkUserSerializer, UserRegisterSerializer
from tools import _auth_jwt


from rest_framework import viewsets, status
from rest_framework.generics import UpdateAPIView, ListAPIView, RetrieveAPIView, CreateAPIView


class UserAuthList(ListAPIView, viewsets.ViewSet):
    # authentication_classes = [_auth_jwt, ]
    # lookup_field = ['pk']
    queryset = Users.objects.exclude(is_superuser=True)
    serializer_class = UsersAuthSerializers


class RegisterCreateView(CreateAPIView, viewsets.ViewSet):
    queryset = Users.objects.all()
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserAuthDetail(UpdateAPIView, RetrieveAPIView, viewsets.ViewSet):
    # lookup_field = ['pk']
    # authentication_classes = [_auth_jwt, ]
    queryset = Users.objects.all()
    serializer_class = UsersAuthDetailSerializer


class WorkViewSet(viewsets.ModelViewSet):
    # lookup_field = ['pk']
    # authentication_classes = [_auth_jwt, ]
    queryset = WorkerUser.objects.all()
    serializer_class = WorkUserSerializer


@csrf_exempt
def get_user_detail(request):
    token = {"token": request.META.get('HTTP_TOKEN')}
    if not token.get('token', None):
        return JsonResponse({
            'code': '-1',
            'message': '请重新登录'
        })

    valid_data = VerifyJSONWebTokenSerializer().validate(token)
    if not valid_data.get('user'):
        return JsonResponse({
            'code': '-1',
            'message': '请重新登录'
        })
    return JsonResponse(valid_data.get('user').get_user_dict())
