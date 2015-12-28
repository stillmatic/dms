from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from checkins import views

urlpatterns = [
    url(r'^checkins/$', views.CheckinList.as_view()),
    url(r'^checkins/(?P<pk>[0-9]+)/$', views.CheckinDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
