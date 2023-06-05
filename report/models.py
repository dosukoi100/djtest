from tkinter import CASCADE
from django.db import models
#バリデーター
from django.core import validators
#Userモデルの呼び出し
from django.contrib.auth import get_user_model

from main.models import Profile

# Create your models here.

#支出のモデル
class Cost(models.Model):
    username = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    member_number = models.ForeignKey(Profile,null=False,blank=False,validators=[validators.MinValueValidator(1),validators.MaxValueValidator(999)],on_delete=models.CASCADE,to_field="member_number",)
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
    '''
    def __str__(self):
        #return self.email
        #ここのidもいらない
        return f"{self.username} (番号は{self.member_number}です。)"
        #return self.member_number
    '''
        
#Chatgtpからのdef __str__関数(特殊関数)の練習用のモデル
class Testchatgtp(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField()
    
    #特殊関数__str__は管理画面などで作成された
    #”モデル名 object”をここで他の文字列で表示します。
    #今回の場合だと作成されたオブジェクト(レコード)に
    #名前と年齢を表示します。
    def __str__(self):
        return f"{self.name} (年齢は{self.age}です)"