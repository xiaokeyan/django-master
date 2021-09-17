from rest_framework.exceptions import AuthenticationFailed
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer


class TokenAuth:
    """
    普通认证
    """
    def authenticate(self, request):
        token = {"token": request.META.get('HTTP_TOKEN')}
        valid_data = VerifyJSONWebTokenSerializer().validate(token)
        user = valid_data['user']
        if user:
            return
        else:
            raise AuthenticationFailed('认证失败')


class TokenAdminAuth:
    """
    admin认证
    """
    def authenticate(self, request):
        token = {"token": request.META.get('HTTP_TOKEN')}
        if not token.get('token', None):
            raise AuthenticationFailed('认证失败')
        valid_data = VerifyJSONWebTokenSerializer().validate(token)
        user = valid_data.get('user', None)
        if not user:
            raise AuthenticationFailed('认证失败')
        # print(user)
        if user.is_superuser:
            return
        else:
            raise AuthenticationFailed('认证失败')
