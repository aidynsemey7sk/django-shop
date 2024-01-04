from rest_framework import serializers
from shop.models import Course, Category


class CourseSerializer(serializers.ModelSerializer):
    category_title = serializers.StringRelatedField()

    class Meta:
        model = Course
        fields = ('title', 'price', 'students_qty', 'reviews_qty', 'category', 'category_title')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)
