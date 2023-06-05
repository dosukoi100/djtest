from django.db import models
#BaseUserManager, AbstractBaseUser 新規でPermissionsMixinインポート
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser ,PermissionsMixin
#idの範囲を絞るためにvalidatorsをインポート
from django.core import validators
# Create your models here.

#＊見方2＊django.contrib.auth.modelsのBaseUserManagerを使用
#テーブル名はUserManager
class UserManager(BaseUserManager):
    #一般ユーザーを作るときのメソッド
    #def create_user(self,id,username, email, password=None):
    def create_user(self,username, email, password=None):
        #idとusernameのValueErrorを追加 
        #ここも削除か
        #if not id:
            #raise ValueError('Users must have an id')
        if not username:
            raise ValueError('Users must have an username')
        #emailがない場合のチェック
        if not email:
            raise ValueError('Users must have an email address')
        #emailがある場合はuserのemailとpasswordを登録する
        #上にidとusernameを追加
        user = self.model(
            #id入らない
            #id=id,
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    #スーパーユーザーを作るときのメソッド
    #この後コマンドラインでスーパーユーザーを作成して
    #emailとpasswordで管理画面にログインできるようにする
    #idとusernameを追加
    #def create_superuser(self,id,username, email, password=None):
    def create_superuser(self,username, email, password=None):
        user = self.create_user(
            #idいらない
            #id=id,
            username=username,
            email=self.normalize_email(email),
            password=password,
        )
        #ここで管理画面に入れるようにしている
        user.is_admin = True
        #user.is_staff = True
        #.is_superuserを追加
        user.is_superuser= True
        user.save(using=self._db)
        return user

#＊見方1＊django.contrib.auth.modelsからAbstractBaseUserを呼び出している
#AbstractBaseUserはユーザーモデルの中でも柔軟性が高い。ただし
#コード量が増える。テーブル名はUser
class User(AbstractBaseUser,PermissionsMixin):
    #idの要素を追加int型としてオートインクリメントとしない
    #id要らない
    '''
    id = models.IntegerField(
        blank=False,
        null=False,
        primary_key=True,
        unique=True,
        validators=[validators.MinValueValidator(1),
                    validators.MaxValueValidator(999)]
    )
    '''
    #username(名前)の追加
    username = models.CharField(max_length=10, unique=True,)
    
    #emailのフィールド
    email = models.EmailField(
        max_length=255,
        #emailが被らないようにしている
        unique=True,
    )
    #アカウントがあればログインできる(Web画面)
    is_active = models.BooleanField(default=True)
    
    #スタッフ権限で管理画面に入れるかを追加
    is_staff = models.BooleanField(default=False)
    
    #管理画面にログインできるか
    is_admin = models.BooleanField(default=False)
    #クラスUserManagerをインスタンス化
    objects = UserManager()
    #デフォルトの管理画面のユーザー名をemailとする
    #管理画面の上、ようこそ(hello)の後に続く文字列
    #また、管理画面ログインフォームのusernameの部分→やっぱりemailとする
    USERNAME_FIELD = 'email'
    
    #USERNAME_FIELD = 'username'

    #ターミナルでのスーパーユーザー作成時にemailとpasswordの他
    #に入力を促す項目にidとusernameを追加
    #ここのidもいらない
    #REQUIRED_FIELDS = ['id','username',]
    REQUIRED_FIELDS = ['username',]
    #REQUIRED_FIELDS = ['id','email',]
    #ここら辺は今はこんな感じだと思えば良いです
    #管理画面でモデルUserからusernameを選択すると
    #トップにusernameとidで表示する
    #オブジェクト(レコードに文字列を返す関数)
    def __str__(self):
        #return self.email
        #ここのidもいらない
        #return f"{self.username} {self.id}"
        return self.username
    
    #Userモデルで使われる関数。ユーザーに特定の権限があるか確
    #認する関数
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    #Userモデルで使われる関数。ユーザーにアプリケーションモジュールの
    #権限があるか確認する際に使われる
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    #Userモデルの属性(usernameやpassword,email,is_activeなど)
    #の1つにis_staffがあります。そのis_staff属性を
    #@propertyデコレータとして使用する
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        #staffとしたいなら
        #return self.is_staff
        return self.is_admin







