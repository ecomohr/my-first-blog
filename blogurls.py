from django.conf.urls import urls
from . import views
from django.shortcuts import render

def post_list(request):
	return render(request, 'blog/post_list.html', {})

url patterns = [
	url(r'^$', views.post_list, name='post_list')
]




