from functools import total_ordering
from django.shortcuts import render,redirect

from django.contrib.auth import get_user,get_user_model


from main.models.profile_models import User,Profile

from report.forms import CostForm,IncomesForm,test1Form,SortForm,CashbookForm

from report.models import Debit,Credit,Sort,Cost,Incomes,Cashbook

# Create your views here.

#報告のインデックス関数
def index(request):
    context = {}
    return render(request,'report/index.html',context)

#-------支出の関数--------------------------

#################################################
#今回はセッションや関数で計算式を実行しない場合の方法です#
#セッションを張らないので一回で確定してしまいますが簡単に#
#モデルにオブジェクト(レコード)を格納するのと、モデルの自#
#由な取り出しを目的にしています。#####################
#################################################

#経費(cost)の入力
def cost(request):
    #GET時
    
    #----ログイン中のユーザー情報を取得----
    user = get_user(request)
    user_id = user.id
    
    #---Profileモデルからログイン中のmember_numberを取得---
    
    #get(pk=user_id)でも良いが、Profileモデルのフィールドu
    #sername_idで指定(こちらが正式)
    member_number = Profile.objects.get(username_id=user_id)
    profile_member_number = member_number.member_number
    
    '''
    #-------検証:モデルの取得について------
    all_model = Profile.objects.all()
    #ログイン中のprofileモデルのオブジェクト(レコード)が帰ってくる
    print(type(member_number))
    #QuerySetで帰ってくる
    print(type(all_model))
    
    #Profileモデルのオブジェクトは関数__str__()で文字列が帰ってくる
    for i in all_model:
        print(i)
    
    #Profileモデルの値はQuerySetで帰ってくる
    for i in all_model.values():
        print(i)
    '''
    
    form = CostForm(request.POST.copy())
    context = {
        'cost_form' : form,#動的ファイルを使う時に使用
        'user_id' : user_id,
        'profile_member_number' : profile_member_number,
        #'profile_type' : print(type(member_number)),#profile_type,
        }
    #POST時
    if request.method == 'POST':
        context['req'] = request.POST.copy()
        dic = context['req']
        
        #---計算式----------------
        list1 = []
        for i in dic:
            if (i == 'username' or i == 'csrfmiddlewaretoken' or i == 'member_number' or i == 'seireki'):
                pass
            else:
                dic[i] = int(dic[i]) #一応int型にする
                list1.append(dic[i])
        print(list1)
        
        n = 0
        for i in list1[:9]:
            n += i 
        
        dic['total'] = n
        #---計算式----------------
        
        form = CostForm(dic)
        
        #---セッション-------------
        request.session['session_data'] = dic
        #---セッション-------------
    
    if form.is_valid():
        #form.save()
        return redirect('../cost_conform/')
        
    return render(request,'report/cost.html',context)

#経費の確認・修正
def cost_conform(request):
    #GET
    context = {}
    dic = {}
    #---セッションの受け取り-------------
    var_session = request.session['session_data']
    #---セッションの受け取り-------------
    
    context = {
        'username' : var_session['username'],
        'member_number' : var_session['member_number'],
        'seireki' : var_session['seireki'],
        'koutuuhi' : var_session['koutuuhi'],
        'shokuhi' : var_session['shokuhi'],
        'youfukuhi' : var_session['youfukuhi'],
        'zeikinn' : var_session['zeikinn'],
        'hoken' : var_session['hoken'],
        'kounetuhi' : var_session['kounetuhi'],
        'yachin' : var_session['yachin'],
        'chuushajoudai' : var_session['chuushajoudai'],
        'zapi' : var_session['zapi'],
        'total' : var_session['total'],
    }
    
    form = CostForm(request.POST.copy())
    
    #POST
    if request.method == 'POST':
        context['req'] = request.POST.copy()
        dic = context['req']
        
        #---計算式----------------
        list1 = []
        for i in dic:
            if (i == 'username' or i == 'csrfmiddlewaretoken' or i == 'member_number' or i == 'seireki'):
                pass
            else:
                dic[i] = int(dic[i]) #一応int型にする
                list1.append(dic[i])
        print(list1)
        
        n = 0
        for i in list1[:9]:
            n += i 
        
        dic['total'] = n
        #---計算式----------------
        
        form = CostForm(dic)
        
        if form.is_valid():
            form.save()
            #---セッションの切断
            del request.session['session_data']
            #---セッションの切断
            return redirect('../cost_thankyou/')
    
    return render(request,'report/cost_conform.html',context)

#経費入力完了
def cost_thankyou(request):
    context = {}
    return render(request,'report/cost_thankyou.html',context)

#-------支出の関数--------------------------

#収入の関数
def incomes(request):
    #GET
    user = get_user(request)
    user_id = user.id
    
    member_number = Profile.objects.get(username_id = user_id)
    profile_member_number = member_number.member_number
    
    form = IncomesForm(request.POST.copy())
    context = {
        'incomes_form' : form,
        'user_id' : user_id,
        'profile_member_number' : profile_member_number,
    }
    
    #POST
    if request.method == 'POST':
        context['req'] = request.POST.copy()
        dic = context['req']
        form = IncomesForm(dic)
        
    if form.is_valid():
        form.save()
    
    return render(request,'report/incomes.html',context)

#-----models.forms.admin.urls.views.htmlの統合練習用----

def test1(request):
    #GET
    user = get_user(request)
    user_id = user.id
    
    member_number = Profile.objects.get(username_id = user_id)
    profile_member_number = member_number.member_number
    
    form = test1Form(request.POST.copy())
    context = {
        'test1_form': form,
        'user_id' : user_id,
        'profile_member_number' : profile_member_number,
    }
    
    #POST
    if request.method == 'POST':
        context['req'] = request.POST.copy()
        dic = context['req']
        form = test1Form(dic)
        
    if form.is_valid():
        form.save()
        
    return render(request,'report/test1.html',context)

##----仕分系------------##

#仕分入力
def sort(request):
    #GET
    
    #ログイン中ユーザーのアカウント情報取得
    user = get_user(request)
    user_id = user.id
    
    #ログイン中のユーザーのProfileモデルのmember_numberを取得
    profile_number = Profile.objects.get(username_id = user_id)
    user_number = profile_number.member_number
    
    #Sortモデルの取得
    sort = Sort.objects.all()
    sort_val = sort.values()
    
    #for i in sort_val:
     #   print(i)
        #print(i['id'],'::',i['debit_id'])
    
    
    
    #Debitモデルの取得
    debit = Debit.objects.all() #モデル総引っ張り
    debit_val = debit.values() #モデルの値を格納
    
    #Creditモデルの取得
    credit = Credit.objects.all() #モデルの総引っ張り
    credit_val = credit.values() #モデルの値を格納
    
    '''
    (検証用)
    print(type(debit))
    print(type(debit_val))
    for i in debit_val:
        print(i)
        for j in i.values():
            print(j)
    '''
    
    #QuerySetは辞書型に近いのでこの方法で値を取り出すことができる
    #debit
    for i in debit_val:
        print(i['id'],'::',i['debit_item'])
        
    #credit
    for i in credit_val:
        print(i['id'],'::',i['credit_item'])
        
    
    
                
    
    #フォーム
    form = SortForm(request.POST.copy())
    
    context = {
        'user_id': user_id,
        'user_number' : user_number,
        'sort_form' : form,
        'debit_val' : debit_val,
        #'sort_val' : sort_val,
        'credit_val' : credit_val,
    }
    
    #POST
    if request.method == 'POST':
        context['req'] = request.POST.copy()
        dic = context['req']
        
        form = SortForm(dic)
        
        #セッション作成
        request.session['session_data'] = dic
        
        if form.is_valid():
            #form.save()
            return redirect('../sort_conform/')
    
    return render(request,'report/sort.html',context)

#仕分確認・訂正
def sort_conform(request):
    #GET
    var_session = request.session['session_data']
    dic = {}
    
    #templates/report/sort_conform.htmlファイルでセレクトボックス
    #を表示するためにdebit,creditモデルのオブジェクトを取得
    
    #Debitモデルの取得
    debit = Debit.objects.all() #モデル総引っ張り
    debit_val = debit.values() #モデルの値を格納
    
    #Creditモデルの取得
    credit = Credit.objects.all() #モデルの総引っ張り
    credit_val = credit.values() #モデルの値を格納
    
    context = {
        'exec_user' : var_session['exec_user'],
        'exec_user_number' : var_session['exec_user_number'],
        'exec_day' : var_session['exec_day'],
        'debit' : int(var_session['debit']),
        'debit_amount' : var_session['debit_amount'],
        'credit' : int(var_session['credit']),
        'credit_amount' : var_session['credit_amount'],
        'comment' : var_session['comment'],
        'debit_val' : debit_val,
        'credit_val' : credit_val,
    }
    form = SortForm(request.POST.copy())
    
    #検証用:セレクトボックスの値を検証してstr型と確認したので
    #int型で渡す
    #print(type(var_session['debit']))
    
    #POST
    if request.method == 'POST':
        context['req'] = request.POST.copy()
        dic = context['req']
        
        form = SortForm(dic)
        
        if form.is_valid():
            form.save()
            del request.session['session_data']
            return redirect('../sort_thankyou/')
    
    return render(request,'report/sort_conform.html',context)

#仕分完了
def sort_thankyou(request):
    context = {}
    return render(request,'report/sort_thankyou.html',context)


##----仕分系------------##

##----収支(Cashbook)--------------------##

#検索画面
def cashbook(request):
    #GET
    
    #全てがいる訳ではないが練習を兼ねて記述
    
    #実行者のUserのidを取得
    exec_user_rec = get_user(request)
    exec_user_id = exec_user_rec.id
    
    #実行者のProfileのmember_number取得
    exec_profile_rec = Profile.objects.get(username_id=exec_user_id)
    exec_number = exec_profile_rec.member_number
    
    #対象者のUserモデルのidを取得
    user_rec = User.objects.get(username='aaaa')#username='aaaa'は仮
    user_id = user_rec.id
    #print(user_id)
    
    ######セレクトボックス用##############################
    user_all_rec = User.objects.all()
    
    profile_all_rec = Profile.objects.all()
    ######セレクトボックス用##############################
    
    #対象者のProfileモデルのmember_numberを取得
    profile_rec = Profile.objects.get(username_id=user_id)
    user_number = profile_rec.member_number
    #print(user_number)
    
    #Incomesモデルの取得
    #オブジェクト全て
    income_rec = Incomes.objects.all()
    income_total_all = income_rec.values('total')
    income_seireki_all = income_rec.values('seireki')
    #print(income_total_all)
    #print(income_seireki_all)
    
    #オブジェクトにフィルターをかける
    income_rec_filter = Incomes.objects.filter(username_id=exec_user_id)#exec_user_idは仮
    income_total_filter = income_rec_filter.values('total')
    income_seireki_filter = income_rec_filter.values('seireki')
    #print(income_total_filter)
    #print(income_seireki_filter)
    
    #オブジェクトにand条件を加える(ForeignKeyフィールドはicontainsは使えない)
    income_rec_filter_and = Incomes.objects.filter(username_id=1,seireki__icontains=2000,member_number_id=1)#数値は仮
    income_total_filter_and = income_rec_filter_and.values('total')
    income_seireki_filter_and = income_rec_filter_and.values('seireki')
    #print(income_total_filter_and)
    #print(income_seireki_filter_and)
    
    
    #Costモデルの取得
    
    #例)Costモデルのtotalをリスト形式で取得する方法
    
    list1 = []
    cost_rec = Cost.objects.all()
    #for i in cost_rec.values():
     #   print(i)
    #print(cost_rec.values('total'))
    for i in cost_rec.values('total'):
        #print(i.values())
        for j in i.values():
            list1.append(j)
    
    #print(list1)
    
    for i in list1:
        #print(i)
        pass
    
    form = CashbookForm(request.POST.copy())
    
    context = {
        #'cashbook_form' : form,
        'exec_number' : exec_number,
        'user_all_rec' : user_all_rec,
        'profile_all_rec' : profile_all_rec,
        
    }
    
    #print('success1')
    #POST
    dic = {}
    if request.method == 'POST':
        context['req'] = request.POST.copy()
        dic = context['req']
        #print(dic)
        #print('success2')
        
        #exec_userのidとexec_user_numberの値を格納
        dic['exec_user'] = exec_user_id
        dic['exec_user_number'] = exec_number
        
        #form = CashbookForm(dic)
        
        l=0
        m=0
        n=0
        for i,j in dic.items():
            #print(i,j)
            if i == 'username':#フォームのusernameのvalue属性の値をlとする
                l=j
            elif i == 'member_number':
                m=j
            elif i == 'seireki':
                n=j
                
        ###income###
        
        #続き)income_rec_filter_andが有る時無い時で条件分岐
        
        #フィルターを掛けてl,m,nの値を格納する。本番環境ならseirekiの方が良い
        income_rec_filter_and = Incomes.objects.filter(username_id=l,member_number_id=m,seireki__icontains=n)
        if income_rec_filter_and :
            print('収入の記録があります')
        
            #取得したオブジェクトのtotalの値を格納(QuerySet)
            income_total_filter_and = income_rec_filter_and.values('total')
            #print(income_total_filter_and)
            
            #QueryDict→dict_valesにする。filterでオブジェクトは1つしか無いのでインデックス番号は0
            income_total = income_total_filter_and[0].values()
            #print(income_total)
            
            #dict_valesの値を変数にして格納
            perpose_income_total = 0
            for i in income_total:
                #print(i)
                perpose_income_total = i
            
            #dicのincome_totalの値をperpose_income_totalとする
            dic['income_total'] = perpose_income_total
            #print(dic)
        else:
            print('収入の記録がありません')
            
        ###cost###
            
        cost_rec_filter_and = Cost.objects.filter(username_id=l,member_number_id=m,seireki__icontains=n)
        if cost_rec_filter_and:
            cost_total_filter_and = cost_rec_filter_and.values('total')
            cost_total = cost_total_filter_and[0].values()
                
            perpose_cost_total = 0 
            for i in cost_total:
                #print(i)
                perpose_cost_total = i
                    
            dic['cost_total'] = perpose_cost_total
            #print(dic)
        else:
            print('支出の記録がありません')
        
        ###cashbookのtotal###
        
        if income_rec_filter_and and cost_rec_filter_and:
            perpose_cashbook_total = perpose_income_total - perpose_cost_total
            dic['total'] = perpose_cashbook_total
            #print(dic)
        else:
            #同じ表示画面上にセッションを貼って受け取ってメッセージを表示させようとしたが
            #うまく表示されなかったのでmessagesで対応
            from django.contrib import messages
            #ここでは特にsettings.pyに記述することはなくてもOK
            #messages.error(request,'記録がありません')
            
            #htmlファイルでmessagesという名のテンプレート変数を受け取れる
            messages.add_message(request,messages.WARNING,'対象者の該当年月がありません。もう一度確認をお願い致します。')
            return redirect('.')
        
        #一応Cashbookのフォームにdicを合わせているので使う
        #特に合わせなくともセッションの受け取り側で加工もOK
        form = CashbookForm(dic)
        
        #セッションを貼る
        request.session['session_data'] = dic
        
        if form.is_valid():
            return redirect('/report/cashbook/conform/')
    
    return render(request,'report/cashbook.html',context)

#確認・変更画面
def cashbook_conform(request):
    #GET
    #セッションの受け取り
    var_session = request.session['session_data']
    dic = {}
    
    #対象者のUserモデルのusernameを取得
    user_rec = User.objects.get(id=var_session['username'])
    user_username_str = user_rec.username
    
    #対象者のProfileのオブジェクト取得
    user_profile_rec = Profile.objects.get(username_id=user_rec.id)
    
    ###########セレクトボックス用###########################
    user_all_rec = User.objects.all()
    
    profile_all_rec = Profile.objects.all()
    ###########セレクトボックス用###########################
    
    
    context = {
        'exec_user' : var_session['exec_user'],
        'exec_user_number' : var_session['exec_user_number'],
        'username' : var_session['username'],
        'member_number' : var_session['member_number'],
        'seireki' : var_session['seireki'],
        'income_total' : var_session['income_total'],
        'cost_total' : var_session['cost_total'],
        'total' : var_session['total'],
        'user_username_str' : user_username_str,
        'user_profile_rec' : user_profile_rec,
        'user_all_rec' : user_all_rec,
        'profile_all_rec' : profile_all_rec,
    }
    
    form = CashbookForm(request.POST.copy())
    
    #POST
    #今回はここでは計算はしません。必要な場合は関数cashbookのPOST以降を参照
    if request.method == 'POST':
        context['req'] = request.POST.copy()
        dic = context['req']
        
        form = CashbookForm(dic)
        
        if form.is_valid():
            form.save()
            del request.session['session_data']
            return redirect('/report/cashbook/thankyou/')
    
    return render(request,'report/cashbook_conform.html',context)

#完了画面
def cashbook_thankyou(request):
    context = {}
    return render(request,'report/cashbook_thankyou.html',context)


##----収支(Cashbook)--------------------##


###----Cashbookモデルのtotalフィールドの総計を取得する----###

#オリジナル
def cashbook_year(request):
    #GET
    
    #ログインユーザー(実行者)(今回は本来は要らない)
    exec_user_rec = get_user(request)
    exec_user_id = exec_user_rec.id
    
    #ログインユーザーの認識番号(今回は本来は要らない)
    exec_user_profile_rec = Profile.objects.get(username_id = exec_user_id)
    exec_user_number = exec_user_profile_rec.member_number
    
    #Userモデルを展開
    user_all_rec = User.objects.all()
    
    #Profileモデルを展開
    profile_all_rec = Profile.objects.all()
    
    context = {
        'exec_user_id' : exec_user_id,
        'exec_user_number' : exec_user_number,
        'user_all_rec' : user_all_rec,
        'profile_all_rec' : profile_all_rec,
    }
    
    #POST
    
    if request.method == 'POST':
        #QuerySetをcontextのreqとしてdicに渡す
        context['req'] = request.POST.copy()
        dic = {}
        dic = context['req']
        #dicのキーを入れて値を格納
        a = dic['username'] #セレクトボックスのバリュー(Userモデルのid)
        b = dic['member_number'] #セレクトボックスのバリュー(Profileモデルのmember_number)
        c = dic['seireki'] #年
    
        
        #対象者のcashbookモデルの該当レコードを取得
        terget_user_cashbook_rec = Cashbook.objects.filter(username_id = a,member_number_id = b,seireki__icontains=c)
        
        if terget_user_cashbook_rec:
        
            list1 = []
            #terget_user_cashbook_recにtotalの値があるものを展開(複数も可)
            for i in terget_user_cashbook_rec.values('total'):
                print(i.values())
                #リストにtotalがある辞書型を格納
                #[{'total':val1},{'total':val2},...]となる
                list1.append(i)
            
            print(list1)
            #####################################################
            #dict_valuesをリストに格納すると以後展開できなくなるので注意#
            #####################################################
            
            n = 0
            #リストを展開して辞書の要素を取り出し
            #辞書のキーでバリューを呼び出し総和を求める
            for i in list1:
                print(i['total'])
                total = i['total']
                n += total
                
            context['total'] = n
            
            print(n)
            
        else:
            from django.contrib import messages
            
            messages.add_message(request,messages.WARNING,'対象者の該当年月がありません。もう一度確認をお願い致します。') 
        
    return render(request,'report/cashbook_year.html',context)

#sum関数
def cashbook_year_def_sum(request):
    #GET
    
    #Userモデルの展開
    user_all_rec = User.objects.all()
    
    #Profileモデルの展開
    profile_all_rec = Profile.objects.all()
    
    #Cashbookモデルのtotalフィールドの総計
    
    from django.db.models import Sum
    #aggregateとSumの試し
    #total = Cashbook.objects.aggregate(total=Sum('total'))['total']
    #total = Cashbook.objects.filter(username_id=1,member_number_id=1,seireki__icontains=2000).aggregate(total=Sum('total'))['total']
    
    
    context = {
        'user_all_rec' : user_all_rec,
        'profile_all_rec' : profile_all_rec,
        #total' : total,
    }
    
    #POST
    
    if request.method == 'POST':
        dic = {}
        context['req'] = request.POST.copy()
        dic = context['req']
        
        #print(dic)
        
        a = dic['username']
        b = dic['member_number']
        c = dic['seireki']
        
        #print(a,b,c,type(a))
        '''
        
        変数をint型にしたいならこちら
        
        a=int(a)
        b=int(b)
        c=int(c)
        
        print(a,b,c,type(a),type(b),type(c))
        '''
        
        #filterメソッドの後にaggregateメソッドとSum関数を使う
        #(値は辞書型なので)キーで値を取得する
        total = Cashbook.objects.filter(username_id=a,member_number_id=b,seireki__icontains=c).aggregate(total=Sum('total'))['total']
        
        #print(total)
        
        if total:
            context['total'] = total
        else:
            from django.contrib import messages
            
            messages.add_message(request,messages.WARNING,'対象者の該当年月がありません。もう一度確認をお願い致します。') 
    
    
    return render(request,'report/cashbook_year_def_sum.html',context)

#生SQL文からの取得
def cashbook_year_sql_sum(request):
    #GET
    
    #Userモデルの展開
    user_all_rec = User.objects.all()
    
    #Profileモデルの展開
    profile_all_rec = Profile.objects.all()
    
    #Cashbookモデルのtotalフィールドの総計
    
    from django.db import connection
    
    #お試しでSQLを叩いてみる
    #with connection.cursor() as cursor:
        #Userモデルのusername_idが1で西暦が2000のtotalの総計を計算
        #cursor.execute("select sum(total) from report_cashbook where username_id = 1 and seireki like '%2000%';")
        #totalはタプルで帰ってくるのでインデックス番号0を指定
        #total = cursor.fetchone()
        #total = cursor.fetchone()[0]
        
        #Userモデルのid=2の情報を取得
        #cursor.execute('select username from main_user where id = 2')
        #total = cursor.fetchall()
        #for i in total:
        #    print(i[0])
        
        #Userモデルの個数
        #cursor.execute('select count(id) from main_user;')
        #total = cursor.fetchone()[0]
    
    context = {
        'user_all_rec' : user_all_rec,
        'profile_all_rec' : profile_all_rec,
        #'total' : total,
    }
    
    #POST
    if request.method == 'POST':
        dic = {}
        context['req'] = request.POST.copy()
        dic = context['req']
        
        a = dic['username']
        b = dic['member_number']
        c = dic['seireki']
        
        #SQLite3の中間一致を使うためにcを整形
        #ここはDBによって違うので注意
        #c = ("'"+'%'+c+'%'+"'")
        c = ('%'+ c +'%')
        
        #print(a,b,c,type(a),type(b),type(c))
        
        #DjangoでのDBに接続してSQL文を実行する
        with connection.cursor() as cursor:
            
            #＊＊＊引数の引き渡しが上手くいかなかったので今回は.format関数で対応＊＊＊
            #＊＊＊コメントアウトも構文的には問題無いみたい。ちなみにMySQLなら'%s'＊＊＊
            #＊＊＊Streamlitの共同溝アプリも参照して下さい＊＊＊
            
            #sql = "select sum(total) from report_cashbook where username_id = ? and member_number_id = ? and seireki like ?;"
            sql = "select sum(total) from report_cashbook where username_id = {} and member_number_id = {} and seireki like '{}' ;".format(a,b,c)
            #cursor.execute(sql,(a,b,c,))
            cursor.execute(sql)
            total = cursor.fetchone()[0]
            
            
        if total:
            context['total'] = total
        else:
            from django.contrib import messages
            
            messages.add_message(request,messages.WARNING,'対象者の該当年月がありません。もう一度確認をお願い致します。') 
            
    return render(request,'report/cashbook_year_sql_sum.html',context)

###----Cashbookモデルのtotalフィールドの総計を取得する----###
 

#-----models.forms.admin.urls.views.htmlの統合練習用----