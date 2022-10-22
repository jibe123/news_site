from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView
)

from .models import Category, News
from .serializers import (
    NewsCreateSerializer,
    NewsListSerializer,
    NewsDetailSerializer,
    NewsDeleteSerializer,
    CategoryCreateSerializer,
    CategoryListSerializer,
    CategoryDetailSerializer,
    CategoryDeleteSerializer
)


class NewsCreateAPIView(CreateAPIView):
    serializer_class = NewsCreateSerializer
    queryset = News.objects.all()


class NewsListAPIView(ListCreateAPIView):
    serializer_class = NewsListSerializer
    queryset = News.objects.all()


class NewsRetrieveAPIView(RetrieveAPIView):
    serializer_class = NewsDetailSerializer
    queryset = News.objects.all()


class NewsUpdateAPIView(UpdateAPIView):
    serializer_class = NewsCreateSerializer
    queryset = News.objects.all()


class NewsDeleteAPIView(DestroyAPIView):
    serializer_class = NewsDeleteSerializer
    queryset = News.objects.all()


class CategoryCreateAPIView(CreateAPIView):
    serializer_class = CategoryCreateSerializer
    queryset = Category.objects.all()


class CategoryListAPIView(ListCreateAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()


class CategoryRetrieveAPIView(RetrieveAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()


class CategoryUpdateAPIView(UpdateAPIView):
    serializer_class = CategoryCreateSerializer
    queryset = Category.objects.all()


class CategoryDeleteAPIView(DestroyAPIView):
    serializer_class = CategoryDeleteSerializer
    queryset = Category.objects.all()


# @api_view(['POST'])
# def news_create(request):
#     serializer = NewsCreateSerializer(data=request.POST)
#     serializer.is_valid()
#
#     category = Category.objects.get(id=serializer.validated_data['category_id'])
#
#     news = News.objects.create(
#         title=serializer.validated_data['title'],
#         category=category,
#     )
#
#     return Response(serializer.data)
