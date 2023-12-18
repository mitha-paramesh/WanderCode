from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
    path('index/',views.demo,name='index'),
    # path('index/',views.demo1,name='index')
]