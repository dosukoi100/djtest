from email.headerregistry import Group
from xml.dom.minidom import Identified
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
#main/models.pyで定義したUserモデルをインポート。追加Profile
from main.models import User,Profile
#main/forms.pyのクラスUserCreationFormをインポート
from main.forms import UserCreationForm

# Register your models here.

#------連続表記するモデルを明示--------

class ProfileInline(admin.StackedInline):
    model = Profile
    #Profileを再度表示するか
    extra = 0

#------連続表記するモデルを明示--------

#管理画面に表示したいモデル(モデル内のカラム名)を明記する
#今回はカスタムユーザーモデルを使用しているのでちょっとコードは多い

#SQLで言うwhere句を使って表示したいカラム名を指定
#UserAdminを継承
class CustomUserAdmin(UserAdmin):
    #連続表示するモデルを指定
    inlines = [ProfileInline,]
    #管理画面でのUserモデル表示と変更画面の項目を表示
    fieldsets = (
        #emailとpasswordを表示
        #idとusernameを追加
        #id要らない
        ('ユーザー情報', {
            'fields': (
                #'id',
                'username',
                'email',
                'password',
            )
        }),
        #ロールの表示。一般ユーザーと管理者を表示
        ('ロール', {
            'fields': (
                'is_active',
                #'is_staff', #追記4/27
                'is_admin',
            )
        })
    )
    
    #リスト一覧を表示すると機に指定する項目
    #今回はemailとis_activeをリスト表示
    #変更するUSERのリストに表示される項目email→usernameに変更
    #Userモデルを選択した際の最初に表示される項目
    list_display = ('username','is_active','is_admin',)
    #ここら辺は今回は設定しませんがUserAdminを継承して色々できます
    list_filter = ()
    ordering = ()
    filter_horizontal = ()
    #検索窓で検索すると、usernameとidから中間一致検索する
    #idはいらないので他のを入れても良い
    search_fields = ['username','id']
    
    #管理画面でユーザーを作成する用に追加
    #idとusernameを追加
    #id入らない
    add_fieldsets = (
        ('新規登録', {
            #'fields': ('id','username','email','password',),
            'fields': ('username','email','password',),
        }),
    )
    
    #＊＊＊ココが無かったので大ハマりした＊＊*組合アプリ＊
    #管理画面でユーザー登録・(変更)が出来ない!!
    add_form = UserCreationForm


class ProfileAdimn(admin.ModelAdmin):
    fieldsets = (
        #emailとpasswordを表示
        #idとusernameを追加
        #id要らない
        ('氏名',{
            'fields':('username',),
            'description':'フルネームを入れて下さい(選択)',
        }),
        ('認識番号',{
            'fields':('member_number',),
            'description':'認識番号を番号を下３桁で入れて下さい',
        }),
        ('電話番号',{
            'fields':('telephone_number',),
            'description':'電話番号を入れて下さい',
        }),
        ('メールアドレス',{
            'fields':('email',),
            'description':'メールアドレスを入れて下さい',
        }),
        ('郵便番号',{
            'fields':('zipcode',),
            'description':'郵便番号を入れて下さい',
        }),
        ('都道府県',{
            'fields':('prefecture',),
            'description':'都道府県を入れて下さい',
        }),
        ('市区町村',{
            'fields':('city',),
            'description':'市区町村を入れて下さい',
        }),
        ('番地',{
            'fields':('address',),
            'description':'番地を入れて下さい',
        }),
    )
    #変更画面の選択時に表示するカラムの種類を選択
    list_display = ('username','member_number',)
    #ここら辺は今回は設定しませんがUserAdminを継承して色々できます
    list_filter = ()
    ordering = ()
    filter_horizontal = ()
    #検索窓で検索すると、member_numberとseirekiから
    #中間一致検索する
    search_fields = ['username','member_number',]
    

#標準の管理画面で表示されるGroupを非表示にする
admin.site.unregister(Group)

#mysite/modelsのUserとmysite/adminのCustomUserAdmin
#を登録する(表示する)
admin.site.register(User,CustomUserAdmin)

#mysite/models/profile_models.pyを表示
#管理画面Usersで表示できるようになったのでコメントアウト
admin.site.register(Profile,ProfileAdimn)
