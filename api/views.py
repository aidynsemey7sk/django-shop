from rest_framework import generics
from shop.models import Course
from api.serializers import CourseSerializer


class CourseAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class DetailCourseAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
