from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import BookInfoSerializer
from .models import BookInfo


# Create your views here.

class BookInfoViewSet(ModelViewSet):

    queryset = BookInfo.objects.all()  # 指明该视图集在查询数据时使用的查询集

    serializer_class = BookInfoSerializer  # 使用的序列化器
