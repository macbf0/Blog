from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'blog_app'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>', post_detail, name='post_detail'),

]