from django.conf.urls import url
from django.urls import path, include, re_path
from django.views.static import serve
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from PayApi import settings
from ZXWL.views import DynamicClassViewSet,\
    DynamicDetailViewSet,\
    DynamicDetailHotViewSet,\
    upload_imag,\
    DynamicClassAdminViewSet,\
    DynamicDetailAdminViewSet
from Users.views import UserAuthList, UserAuthDetail, WorkViewSet, get_user_detail, RegisterCreateView
from trialRun.views import CreateClienteleInfoAPiView


router = routers.DefaultRouter()
router.register('DynamicClass', DynamicClassViewSet, basename='DynamicClassViewSet')
router.register('DynamicClassAdmin', DynamicClassAdminViewSet, basename='DynamicClassAdminViewSet')

router.register('DynamicDetail', DynamicDetailViewSet, basename='DynamicDetailViewSet')
router.register('DynamicDetailAdmin', DynamicDetailAdminViewSet, basename='DynamicDetailAdminViewSet')

router.register('DynamicDetailHot', DynamicDetailHotViewSet, basename='DynamicDetailHotViewSet')
router.register('UserAuthList', UserAuthList, basename='UserAuthList')
router.register('users-detail', UserAuthDetail, basename='Users-detail')
router.register('users-WorkViewSet', WorkViewSet, basename='WorkViewSet')
router.register('RegisterCreateView', RegisterCreateView, basename='RegisterCreateView')

router.register('CreateClienteleInfoAPiView', CreateClienteleInfoAPiView, basename='CreateClienteleInfoAPiView')


urlpatterns = [
    path('', include(router.urls)),
    path('auth_url', include('rest_framework.urls')),
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^login/', obtain_jwt_token),
    url('upload_image', upload_imag),
    url('get_user_detail/', get_user_detail)
]
