
#from tkinter import CASCADE
from tkinter import CASCADE
from django.db import models
#バリデーター
from django.core import validators
#Userモデルの呼び出し
from django.contrib.auth import get_user_model
#Profileモデルの呼び出し
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

#収入のモデル 
class Incomes(models.Model):
    username = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    member_number = models.ForeignKey(Profile,null=False,blank=False,validators=[validators.MinValueValidator(1),validators.MaxValueValidator(999)],on_delete=models.CASCADE,to_field="member_number",)
    seireki = models.IntegerField(null=False,blank=False,validators=[validators.MinValueValidator(200001),validators.MaxValueValidator(299912)])
    salary = models.IntegerField(default=0,null=False,blank=False)
    bonus = models.IntegerField(default=0,null=False,blank=False)
    temporary_income = models.IntegerField(default=0,null=False,blank=False)
    total = models.IntegerField(null=False,blank=False)
    create_at = models.DateField(auto_now_add=True,)
    update_at = models.DateField(auto_now=True,)
    
    def __str__(self):
        return f"{self.username}の{self.seireki}収入です"
    

#-----models.forms.admin.urls.views.htmlの統合練習用----

class test1(models.Model):
    username = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    member_number = models.ForeignKey(Profile,null=False,blank=False,validators=[validators.MinValueValidator(1),validators.MaxValueValidator(999)],on_delete=models.CASCADE,to_field="member_number",)
    walks = models.IntegerField(default=0,null=False,blank=False,)
    insert_day = models.DateField(help_text='記入日')
    create_at = models.DateField(auto_now_add=True,)
    update_at = models.DateField(auto_now=True,)
    
    def __str__(self):
        return f"{self.username}の{self.insert_day}の歩いた歩数です"


#借方モデル←
class Debit(models.Model):
    debit_item = models.CharField(max_length=100)
    
    def __str__(self):
        return f"借方項目は{self.debit_item}です"   

#貸方モデル→
class Credit(models.Model):
    credit_item = models.CharField(max_length=100)
    
    def __str__(self):
        return f"貸方項目は{self.credit_item}です"
    
#仕分けモデル
class Sort(models.Model):
    exec_user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    exec_user_number = models.ForeignKey(Profile,null=False,blank=False,validators=[validators.MinValueValidator(1),validators.MaxValueValidator(999)],on_delete=models.CASCADE,to_field="member_number",)
    exec_day = models.DateField(help_text='仕分実行日')
    debit = models.ForeignKey(Debit,on_delete=models.CASCADE)
    debit_amount = models.IntegerField(null=False,blank=False,)
    credit = models.ForeignKey(Credit,on_delete=models.CASCADE)
    credit_amount = models.IntegerField(null=False,blank=False,)
    comment = models.TextField()
    create_at = models.DateField(auto_now_add=True,)
    update_at = models.DateField(auto_now=True,)
    
    def __str__(self):
        return f"{self.exec_day}の{self.comment}の仕分けです"



#-----models.forms.admin.urls.views.htmlの統合練習用----

    
    
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