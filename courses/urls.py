from django.urls import path
from . import views   #nokta dediğimizde aynı dizinde olduğumuzu kastederiz

#http://127.0.0:8000/  -->anasayfa
#http://127.0.0:8000/home   -->anasayfa
#http://127.0.0:8000/kurslar  -->kurs listesi

urlpatterns = [  #url kalıbı
     path('',views.index),
    
     path('<kurs_id>',views.details,name='course_details'),
     path('kategori/<int:category_id>',views.   getCoursesByCategoryId),
     path('kategori/<str:category_name>',views.getCoursesByCategory, name='courses_by_category'),
     
]
#views.home dediğimizde ilgili dosyadan ilgili metodları almış oluyoruz diğer türlü hata verir
#yukarıdan aşağı filtreleme yapıldığı için ilk eşleşen viewi açar