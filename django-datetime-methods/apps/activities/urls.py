from django.conf.urls import url
import views


urlpatterns = [
    # urls for Activity
    url(r'^$', views.activity_list, name='activity_list'),
    url(r'^tag/$', views.activity_tag, name='activity_tag'),
    url(r'^expression/$', views.activity_expression, name='activity_expression'),
    url(r'^casewhen/$', views.activity_casewhen, name='activity_casewhen'),
]
