from django.urls import path
from app.views import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('app_list/', app_list, name='app_list'),
    path('app_list/<int:rubric_id>/', app_detail, name='app_detail'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('manage/', manage, name='manage'),
    path('manage/<int:pk>/update/',  update, name='update'),
    path('manage/<int:pk>/delete/', delete, name='delete'),

    path('contact/', contact, name='contact'),
]