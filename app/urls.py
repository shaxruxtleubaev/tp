from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_page, name='home_page'),
    path('app_list/', app_list, name='app_list'),
    path('app_list/<int:rubric_id>/', app_detail, name='app_detail'),
    path('create/', ProductCreateView, name='create'),
    path('manage/', manage, name='manage'),
    path('manage/<int:pk>/update/',  update, name='update'),
    path('manage/<int:pk>/delete/', delete, name='delete'),

    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('repo/', report, name='report'),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''