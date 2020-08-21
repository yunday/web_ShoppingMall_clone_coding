from django.db import models

# Create your models here.
class UserInfo(models.Model):
    no = models.AutoField(primary_key=True)
    id = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=15, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    birth = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_info'