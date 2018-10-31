from django.conf.urls import url, include
from main import views as main_views
from django.contrib.auth import views as auth_views


app_name = 'main'
urlpatterns = [
#    url(r'^$', main_views.base, name='base' ),
    url(r'^$', main_views.index, name='index' ),
]
