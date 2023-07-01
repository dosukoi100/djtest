from django.contrib import admin
#from djangoproject.test1_basic_django.report.models import Testchatgtp

#report/models.pyからcostモデルを呼び出す
from report.models import Cost,Incomes,test1,Debit,Credit,Sort
from report.models import Testchatgtp

# Register your models here.

#costモデルの表示
class CostAdmin(admin.ModelAdmin):
    fieldsets = (
        ('氏名',{
            'fields':('username',),
            'description':'組合員のフルネームを入れて下さい',
        }),
        ('組合番号',{
            'fields':('member_number',),
            'description':'組合番号を番号を下３桁で入れて下さい',
        }),
        ('西暦',{
            'fields':('seireki',),
            'description':'西暦を月まで入れて下さい。(例:2010年08月は、201008)',
        }),
        ('交通費',{
            'fields':('koutuuhi',),
            'description':'交通費を入れて下さい',
        }),
        ('食費',{
            'fields':('shokuhi',),
            'description':'食費を入れて下さい',
        }),
        ('洋服代',{
            'fields':('youfukuhi',),
            'description':'洋服代を入れて下さい',
        }),
        ('税金',{
            'fields':('zeikinn',),
            'description':'税金を入れて下さい',
        }),
        ('保険代',{
            'fields':('hoken',),
            'description':'保険代を入れて下さい',
        }),
        ('光熱費',{
            'fields':('kounetuhi',),
            'description':'光熱費を入れて下さい',
        }),
        ('住居費',{
            'fields':('yachin',),
            'description':'住居費を入れて下さい',
        }),
        ('駐車場代',{
            'fields':('chuushajoudai',),
            'description':'駐車場代を入れて下さい',
        }),
        ('雑費',{
            'fields':('zapi',),
            'description':'雑費を入れて下さい',
        }),
        ('総支出',{
            'fields':('total',),
            'description':'総支出を入れて下さい',
        }),
    )

    #変更画面の選択時に表示するカラムの種類を選択
    list_display = ('member_number','username','seireki',)
    
    #ちなみにCostモデル(report_costテーブル)にはmember_numberは無く
    #member_number_idが有りそのmember_number_idを表示させる事を
    #ここで指定することは出来る
    
    #list_display = ('member_number_id','username','seireki',)
    
    
    #OneToOneフィールドやForeignKeyフィールドはここで
    #指定すると良い
    list_filter = ('username','member_number',)
    
    #オブジェクト(レコード)の並び順を指定。-を付けると降順
    ordering = ('-member_number',)
    
    #ManyToManyフィールドで使う
    filter_horizontal = ()
    
    #検索窓で検索する#中間一致検索する
    #OneToOneフィールドやForeignKeyフィールドを
    #ここで指定するとエラーとなる場合はlist_filterでその部分は
    #指定する
    #例）
    #search_fields = ['username','member_number','seireki',]
    #この場合はusernameとmember_numberはlist_filterで指定する
    search_fields = ['seireki',]

class IncomesAdmin(admin.ModelAdmin):
    fieldsets = (
        ('氏名',{
            'fields':('username',),
            'description':'組合員のフルネームを入れて下さい',
        }),
        ('組合番号',{
            'fields':('member_number',),
            'description':'組合員番号を入れて下さい',
        }),
        ('年月',{
            'fields':('seireki',),
            'description':'西暦(年月)を入れて下さい(例:2001年1月なら200101)',
        }),
        ('給料収入',{
            'fields':('salary',),
            'description':'当月の給与収入を入れて下さい',
        }),
        ('ボーナス',{
            'fields':('bonus',),
            'description':'ボーナスがあれば入れて下さい',
        }),
        ('臨時収入',{
            'fields':('temporary_income',),
            'description':'臨時収入があれば入れて下さい',
        }),
        ('総収入',{
            'fields':('total',),
            'description':'当月の総収入を入れて下さい',
        }),
    )
    
    list_display = ('member_number','username','seireki','create_at','update_at',)
    
    list_filter = ('username',)
    
    ordering = ('-member_number',)
    
    search_fields = ['seireki',]
    
#-----models.forms.admin.urls.views.htmlの統合練習用----
#test1歩数の入力
class test1Admin(admin.ModelAdmin):
    fieldsets = (
        ('氏名',{
            'fields':('username',),
            'description':'組合員のフルネームを入れて下さい',
        }),
        ('組合番号',{
            'fields':('member_number',),
            'description':'組合員番号を入れて下さい',
        }),
        ('歩数',{
            'fields':('walks',),
            'description':'歩数を入れて下さい',
        }),
        ('歩いた日',{
            'fields':('insert_day',),
            'description':'歩いた日を選択して下さい',
        }),
    )
    
    list_display = ('username','member_number','walks','insert_day','create_at','update_at',)
    list_filter = ('username',)
    ordering = ('-insert_day',)
    search_fields = ['insert_day']
    
#借方(Debit)
class DebitAdmin(admin.ModelAdmin):
    fieldsets = (
        ('借方項目', {
            "fields": ('debit_item',),
            'description':'借方を追加・確認・変更して下さい',
        }),
    )
    
    list_display = ('debit_item',)
    ordering = ('-debit_item',)
    search_fields = ['debit_item']
    

#貸方(Credit)
class CreditAdmin(admin.ModelAdmin):
    fieldsets = (
        ('貸方項目', {
            "fields": ('credit_item',),
            'description':'貸方を追加・確認・変更して下さい',
        }),
    )
    
    list_display = ('credit_item',)
    ordering = ('-credit_item',)
    search_fields = ['credit_item']
    
#仕分(Sort)
class SortAdmin(admin.ModelAdmin):
    fieldsets = (
        ('実行者', {
            "fields": ('exec_user',),
            'description':'仕分入力者',
        }),
        ('実行者番号', {
            "fields": ('exec_user_number',),
            'description':'仕分入力者の番号',
        }),
        ('実行日', {
            "fields": ('exec_day',),
            'description':'仕分実行日',
        }),
        ('借方項目', {
            "fields": ('debit',),
            'description':'借方項目の選択',
        }),
        ('借方金額', {
            "fields": ('debit_amount',),
            'description':'借方金額の入力',
        }),
        ('貸方項目', {
            "fields": ('credit',),
            'description':'貸方項目の選択',
        }),
        ('貸方金額', {
            "fields": ('credit_amount',),
            'description':'貸方金額の入力',
        }),
        ('仕分の内容', {
            "fields": ('comment',),
            'description':'仕分内容の記述',
        }),
    )
    
    list_display = ('exec_user','exec_day','comment',)
    ordering = ('-exec_day',)
    search_fields = ['exec_user','exec_day',]
    

#-----models.forms.admin.urls.views.htmlの統合練習用----


#管理画面にCostモデルを表示可能とする
admin.site.register(Cost,CostAdmin)

admin.site.register(Incomes,IncomesAdmin)

#-----models.forms.admin.urls.views.htmlの統合練習用----
#歩数計
admin.site.register(test1,test1Admin)

#借方(Debit)
admin.site.register(Debit,DebitAdmin)

#貸方(Credit)
admin.site.register(Credit,CreditAdmin)

#仕分(Sort)
admin.site.register(Sort,SortAdmin)

#-----models.forms.admin.urls.views.htmlの統合練習用----

admin.site.register(Testchatgtp)


