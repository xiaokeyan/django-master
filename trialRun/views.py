from rest_framework import viewsets
from rest_framework.generics import CreateAPIView

from .trial_run_serializers import ClienteleInfoSerializer
from .models import ClienteleInfos


class CreateClienteleInfoAPiView(viewsets.ViewSet, CreateAPIView):
    serializer_class = ClienteleInfoSerializer
    queryset = ClienteleInfos.objects.all()
