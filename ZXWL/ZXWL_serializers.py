from rest_framework import serializers
from datetime import datetime


from ZXWL.models import DynamicClass, DynamicDetail


class DynamicDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='DynamicDetailViewSet-detail', lookup_field='pk')

    class Meta:
        model = DynamicDetail
        fields = ['id', 'title', 'content', 'overview', 'status', 'is_hot', 'url', 'dynamic_class_id']
        # partial = True


class DynamicClassSerializers(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='DynamicClassViewSet-detail', lookup_field='pk')
    # class_dynamic = serializers.HyperlinkedIdentityField(
    #      many=True,
    #      view_name='DynamicDetailViewSet-detail',
    #      allow_null=True,
    # )

    class_dynamic = DynamicDetailSerializer
    create_time = serializers.DateTimeField(
        format='%Y-%m-%d %H:%M:%S',
        allow_null=True,
        default=datetime.now()
    )

    class Meta:
        model = DynamicClass
        fields = ['id', 'name', 'url', 'create_time', 'update_time', 'status', 'info', 'class_dynamic']
        depth = 1
        partial = True
