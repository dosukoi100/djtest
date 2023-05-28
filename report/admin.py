from django.contrib import admin

#report/models.pyからcostモデルを呼び出す
from report.models import Cost

# Register your models here.

#管理画面にCostモデルを表示可能とする
admin.site.register(Cost)
