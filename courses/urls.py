from django.urls import path
from . import views   #nokta dediğimizde aynı dizinde olduğumuzu kastederiz

#http://127.0.0:8000/  -->anasayfa
#http://127.0.0:8000/home   -->anasayfa
#http://127.0.0:8000/kurslar  -->kurs listesi

urlpatterns = [  #url kalıbı
     path('',views.index, name="index"),
     path('search',views.search ,name="search"),
     path('create-course',views.create_course ,name="create_course"),
     path("course-list", views.course_list, name="course_list"),
     path("course-edit/<int:id>",views.course_edit,name="course_edit"),
     path("course-delete/<int:id>",views.course_delete,name="course_delete"),
     path('upload', views.upload, name="upload_image"),
     path('kurslar/<slug:slug>',views.details,name='course_details'),   
     path('kategori/<slug:slug>',views.getCoursesByCategory, name='courses_by_category'),
     
]
#views.home dediğimizde ilgili dosyadan ilgili metodları almış oluyoruz diğer türlü hata verir
#yukarıdan aşağı filtreleme yapıldığı için ilk eşleşen viewi açar