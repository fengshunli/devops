from django.db import models


# Create your models here.
class TbEurekaManager(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=100)
    eureka_url = models.CharField(max_length=200)
    manager = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_eureka_manager'