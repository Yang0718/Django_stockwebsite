from django.contrib import admin
from .models import StockDB # 先把做好的DB import進來

admin.site.register(StockDB) # 這行就能把model弄進admin中並操作這db了



