from django.conf.urls import url
from . import views

urlpatterns = [

    ###git spring cloud####
    #dep
    url(r'^api/dep/git/get_proj_n','release_system.new_proj.views.get_proj_n'),
    url(r'^api/dep/git/get_proj_dp','release_system.new_proj.views.get_proj_dp'),
    url(r'^api/dep/git/get_proj_h','release_system.new_proj.views.get_proj_h'),
    url(r'^api/dep/git/maven','release_system.new_proj.views.maven'),
    url(r'^api/dep/git/staging_maven','release_system.new_proj.views.staging_maven'),
    url(r'^api/dep/git/deploy_sc_dep','release_system.new_proj.views.deploy_sc_dep'),
    url(r'^api/dep/git/view_k8s_pods','release_system.new_proj.views.view_k8s_pods'),
    url(r'^api/dep/git/get_app_v','release_system.new_proj.views.get_app_v'),
    #ops
    url(r'^api/ops/git/get_proj_n','release_system.new_proj.views.get_proj_n'),
    url(r'^api/ops/git/get_proj_dp','release_system.new_proj.views.get_proj_dp'),
    url(r'^api/ops/git/get_proj_h','release_system.new_proj.views.get_proj_h'),
    url(r'^api/ops/git/maven','release_system.new_proj.views.maven'),
    url(r'^api/ops/git/deploy_sc_ops','release_system.new_proj.views.deploy_sc_ops'),
    url(r'^api/ops/git/view_k8s_pods','release_system.new_proj.views.view_k8s_pods'),
    
    ###git app ####
    #dep
    url(r'^api/dep/git/deploy_app_dep','release_system.new_proj.views.deploy_app_dep'),
    #ops
    url(r'^api/ops/git/deploy_app_dep','release_system.new_proj.views.deploy_app_ops'),
]
