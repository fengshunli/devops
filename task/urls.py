from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="task/index"),
    url(r'^add$', views.add, name="task/add"),
    url(r'^history$', views.history, name="task/history"),

]
