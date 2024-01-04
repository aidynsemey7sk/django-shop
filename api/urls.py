from django.urls import path
from .views import CourseAPIView, DetailCourseAPIView, CategoryAPIView


urlpatterns = [
    path('', CourseAPIView.as_view()),
    path('<int:pk>/', DetailCourseAPIView.as_view()),
    path('category/', CategoryAPIView.as_view()),
]