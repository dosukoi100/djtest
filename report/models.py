from django.db import models
#バリデーター
from django.core import validators
#Userモデルの呼び出し
from django.contrib.auth import get_user_model

# Create your models here.

#支出のモデル
class Cost(models.Model):
    username = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    member_number = models.IntegerField(null=False,blank=False,validators=[validators.MinValueValidator(1),validators.MaxValueValidator(999)])
    seireki = models.IntegerField(null=False,blank=False,validators=[validators.MinValueValidator(200001),validators.MaxValueValidator(299912)])
    koutuuhi = models.IntegerField(default=0,null=False,blank=False)
    shokuhi = models.IntegerField(default=0,null=False,blank=False)
    youfukuhi = models.IntegerField(default=0,null=False,blank=False)
    zeikinn = models.IntegerField(default=0,null=False,blank=False)
    hoken = models.IntegerField(default=0,null=False,blank=False)
    kounetuhi = models.IntegerField(default=0,null=False,blank=False)
    yachin = models.IntegerField(default=0,null=False,blank=False)
    chuushajoudai = models.IntegerField(default=0,null=False,blank=False)
    zapi = models.IntegerField(default=0,null=False,blank=False)
    total = models.IntegerField(null=False,blank=False)