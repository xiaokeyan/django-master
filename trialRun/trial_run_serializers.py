from rest_framework import serializers, exceptions


from .models import ClienteleInfos
from tools.ID_check import check_id_data, check_id_length
from tools.check_mobile import is_phone


class ClienteleInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClienteleInfos
        fields = '__all__'

    card = serializers.CharField(max_length=18, min_length=18, error_messages={
        'max-length': '身份证长度必须是18',
        'min-length': '身份证长度必须是18！'
    })
    mobile = serializers.CharField(max_length=11, min_length=11, error_messages={
        'max-length': '手机号长度必须是11位！',
        'min-length': '手机号长度必须是11位！'
    })

    def validate_card(self, ID):
        if not check_id_length(ID):
            raise exceptions.ValidationError('只支持18位身份证!')

        if not check_id_data(ID):
            raise exceptions.ValidationError('检查身份证输入是否正确!')

        return ID

    def validate_mobile(self, mobile):
        if is_phone(mobile):
            return mobile
        raise exceptions.ValidationError('手机号不合法!')




