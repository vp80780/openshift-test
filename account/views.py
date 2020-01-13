from django.shortcuts import render

# Create your views here.
from .models import Temp
from .serializers import TempSerializer
from rest_framework import viewsets
from .custom_deco import role_required
class TempViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Temp.objects.all()
    serializer_class = TempSerializer
    #
    # @role_required(allowed_roles=['admin'])
    # def get_queryset(self):
    #     q = self.queryset
    #     if 'admin' in self.request.role:
    #         return q
    #     return q.none()