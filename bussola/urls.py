from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/', views.do_login, name='login'),
	url(r'^logout/', views.do_logout, name='logout'),
	url(r'^cadastro/', views.cadastro, name='cadastro'),
	url(r'^estabelecimento/', views.estabelecimento, name='estabelecimento'),
	url(r'^lugares/', views.lugares, name='lugares'),
]