from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="release/index"),
    url(r'^inadd$', views.inadd, name="release/inadd"),
    url(r'^inaddshell$', views.inadd_shell, name="release/inaddshell"),
    url(r'^once$', views.once, name="release/once"),
    url(r'^history$', views.history, name="release/history"),
    url(r'^details$', views.details, name="release/details"),

]
