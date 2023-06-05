from django.contrib import admin
#from djangoproject.test1_basic_django.report.models import Testchatgtp

#report/models.pyからcostモデルを呼び出す
from report.models import Cost
from report.models import Testchatgtp

# Register your models here.

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

#管理画面にCostモデルを表示可能とする
admin.site.register(Cost,CostAdmin)

admin.site.register(Testchatgtp)
