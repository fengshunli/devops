from django.conf.urls import url, include
from . import views



urlpatterns = [
    url(r'^api/dep/get_proj_n','release_system.views.get_proj_n'),
    url(r'^api/ops/get_proj_n','release_system.views.get_proj_n'),
    url(r'^api/dep/get_proj_h','release_system.views.get_proj_h'),
    url(r'^api/ops/get_proj_h','release_system.views.get_proj_h'),
    url(r'^api/dep/read','release_system.views.read_file'),
    url(r'^api/ops/read','release_system.views.read_file'),


    #dep
    url(r'^api/dep/test','release_system.views.test'),
    url(r'^api/dep/downloadcode','release_system.views.downloadcode'),
    url(r'^api/dep/staging','release_system.views.staging'),
    
    #ops
    url(r'^api/ops/staging','release_system.views.staging'),
    url(r'^api/ops/full','release_system.views.full'),
    url(r'^api/ops/add','release_system.views.add'),
    url(r'^api/ops/roll','release_system.views.roll'),
    url(r'^api/ops/restart','release_system.views.restart'),
    url(r'^api/ops/nginx','release_system.views.nginx'),
   
    ###spring cloud####
    #dep
    url(r'^api/dep/sc/get_proj_n','release_system.spring.views.get_proj_n'),
    url(r'^api/dep/sc/get_proj_dp','release_system.spring.views.get_proj_dp'),
    url(r'^api/dep/sc/maven','release_system.spring.views.maven'),
    url(r'^api/dep/sc/deploy','release_system.spring.views.deploy_dep'),
    #ops
    url(r'^api/ops/sc/get_proj_n','release_system.spring.views.get_proj_n'),
    url(r'^api/ops/sc/get_proj_dp','release_system.spring.views.get_proj_dp'),
    url(r'^api/ops/sc/maven','release_system.spring.views.maven'),
    url(r'^api/ops/sc/deploy','release_system.spring.views.deploy_ops'),

    ###git spring cloud####


    url(r'^git/', include('release.git.urls')),
]
