from rest_framework import serializers
from shop.models import Course, Category


class CourseSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Course
        fields = ('title', 'price', 'students_qty', 'reviews_qty', 'category', 'created_at')
