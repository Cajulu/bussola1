from django.conf.urls import include, url
from . import views 

urlpatterns = [
	url(r'^$', views.index),
	url(r'^login/', views.login),
	url(r'^cadastro/', views.cadastro),
	url(r'^fale_conosco/', views.fale_conosco),
	url(r'^estabelecimento/', views.estabelecimento),
	url(r'^lugares/', views.lugares),
	url(r'^sobre_nos/', views.sobre_nos),
	url(r'^sub_categoria/', views.sub_categoria),
]