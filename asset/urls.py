from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="asset/index"),
    url(r'^inadd$', views.inadd, name="asset/inadd"),
    url(r'^add$', views.add, name="asset/add"),
    url(r'^list$', views.lists, name="asset/list"),

]
