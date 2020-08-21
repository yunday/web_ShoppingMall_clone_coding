from django.db import models

# Create your models here.
class ClothesTb(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    price = models.IntegerField()
    stock = models.IntegerField()
    category = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clothes_tb'