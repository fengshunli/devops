from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="task/index"),
    url(r'^inadd$', views.inadd, name="task/inadd"),
    url(r'^inaddshell$', views.inadd_shell, name="task/inaddshell"),
    url(r'^once$', views.once, name="task/once"),
    url(r'^history$', views.history, name="task/history"),
    url(r'^details$', views.details, name="task/details"),

]
