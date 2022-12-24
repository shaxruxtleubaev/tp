from django.urls import path
from app.views import *

urlpatterns = [
    path('', home_page, name='home_page')
]