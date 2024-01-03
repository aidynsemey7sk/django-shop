from django.urls import path
from shop.views import index, single_course

app_name = 'shop'

urlpatterns = [
    path('', index, name='index'),
    path('<int:course_id>', single_course, name='single_course'),
]