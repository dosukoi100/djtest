from django.shortcuts import render,redirect

from django.contrib.auth import get_user,get_user_model


from main.models.profile_models import Profile

from report.forms import CostForm,IncomesForm,test1Form,SortForm

from report.models import Debit,Credit,Sort

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
    return render(request,'report/sort_thankyou.html')


##----仕分系------------##
 

#-----models.forms.admin.urls.views.htmlの統合練習用----