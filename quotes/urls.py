from django.urls import path
from . import  views
urlpatterns = [
    path('', views.home, name='home'), # 引號裡面留白是因為這邊在做首頁。views.home的home指的是views.py裡面的function。
    path('about.html', views.about, name='about'),  # name是用在網址連結。這也是django與html不同之處
                                                    # 用意在於，前面的about.html可以改成其他網址如about-me.html，但是因為沒動到name，所以連結不會跑掉
    path('add_stock.html', views.add_stock, name='add_stock'),
    path('delete/<stock_id>', views.delete, name='delete'),
    path('delete_stock.html', views.delete_stock, name='delete_stock'),
]

