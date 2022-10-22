from rest_framework import serializers

from .models import News, Category


class NewsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'description', 'author', 'category')


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class NewsDetailSerializer(serializers.ModelSerializer):
    category_title = serializers.SerializerMethodField()

    def get_category_title(self, obj):
        return obj.category.title

    class Meta:
        model = News
        fields = '__all__'


class NewsDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id',)


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id',)