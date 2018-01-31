from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=30)
    project_group_id = models.IntegerField()
    leader = models.CharField(max_length=10)
    project_type = models.IntegerField()
    scm_type = models.IntegerField()
    scm_url = models.CharField(max_length=100)
    remark = models.CharField(max_length=200, blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_project'


class ProjectGroup(models.Model):
    name = models.CharField(max_length=30)
    remark = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_project_group'
