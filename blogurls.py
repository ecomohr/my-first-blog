from django.conf.urls import urls
from . import views

url patterns = [
	url(r'^$', views.post_list, name='post_list')
]




