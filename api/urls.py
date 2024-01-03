from django.urls import path
from .views import CourseAPIView, DetailCourseAPIView


urlpatterns = [
    path('', CourseAPIView.as_view()),
    path('<int:pk>/', DetailCourseAPIView.as_view()),
]