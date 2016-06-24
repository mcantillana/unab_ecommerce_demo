from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^category/(?P<category_id>\d+)/$', views.category),
]