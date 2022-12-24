from django.urls import path
from app.views import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('app_list/', app_list, name='app_list'),
    path('app_list/<int:rubric_id>/', app_detail, name='app_detail')
]