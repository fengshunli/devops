from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="release/project/index"),
    url(r'^add$', views.add, name="release/project/add"),
    url(r'^add_project$', views.add_project, name="release/project/add_project"),
]
