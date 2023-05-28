#プロフィール情報もモデルです

from django.db import models
from django.contrib.auth import get_user_model
from main.models import User


#int型の範囲を絞るためにvalidatorsをインポート
from django.core import validators

class Profile(models.Model):
    username = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    member_number = models.IntegerField(unique=True,default=0,null=False,blank=False,
        validators=[validators.MinValueValidator(1),
                    validators.MaxValueValidator(999)])
    telephone_number = models.BigIntegerField(null=False,blank=False,)
    email = models.CharField(default="",max_length=40)
    #email = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    #郵便番号 
    zipcode = models.CharField(default="",max_length=8) 
    #都道府県 
    prefecture = models.CharField(default="",max_length=6) 
    #市区町村 
    city = models.CharField(default="",max_length=100) 
    #町名等 
    address = models.CharField(default="",max_length=100) 