from django.conf.urls import url
from locations import views

urlpatterns = [
    url(r'^checkins/$', views.checkin_list),
    url(r'^checkins/(?P<pk>[0-9]+)/$', views.checkin_detail),
]