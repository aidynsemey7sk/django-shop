from rest_framework import generics
from shop.models import Course, Category
from api.serializers import CourseSerializer, CategorySerializer
from api.permissions import IsAuthorOrReadOnly


class CourseAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CategoryAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DetailCourseAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
