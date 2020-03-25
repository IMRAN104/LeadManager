from django.conf.urls import include, url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.course_list),
    path('<pk>/', views.course_details, name='course'),
]
