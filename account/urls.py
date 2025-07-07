from django.urls import path
from . import views   #nokta dediğimizde aynı dizinde olduğumuzu kastederiz

#http://127.0.0:8000/  -->anasayfa
#http://127.0.0:8000/home   -->anasayfa
#http://127.0.0:8000/kurslar  -->kurs listesi

urlpatterns = [  #url kalıbı
     path('login',views.user_login, name="user_login"),
     path('register',views.user_register, name="user_register"),
     path('logout',views.user_logout, name="user_logout"),
    
]
#views.home dediğimizde ilgili dosyadan ilgili metodları almış oluyoruz diğer türlü hata verir
#yukarıdan aşağı filtreleme yapıldığı için ilk eşleşen viewi açar