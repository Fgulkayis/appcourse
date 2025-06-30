from datetime import date,datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Course,Category
# Create your views here.
data= {
    "programlama":"programlama kategorisine ait kurslar ",
    "web-gelistirme":"web gelistirme kategorisine ait kurslar",
    "mobil":"mobil kategorisine ait kurslar",
}
db={
    "courses":[
        {
        "title":"javascript kursu",
        "description":"javascript kurs açıklaması",
        "imageUrl":"2.jpg",
        "slug":"javascript-kursu",
         "date": datetime.now(),
         "isActive":True,
         "isUpdated": False
         },
         {
         "title":"python kursu",
        "description":"python kurs açıklaması",
        "imageUrl":"1.jpg",
        "slug":"python-kursu",
         "date": date(2022,9,10),
         "isActive":True,
         "isUpdated": False
         },
         {   
        "title":"web-geliştirme kursu",
        "description":"web geliştirme kurs açıklaması",
        "imageUrl":"3.jpg",
        "slug":"web-gelistirme-kursu",
         "date": date(2022,10,10),
         "isActive":True,
         "isUpdated": False
         }

    ],
    
}
def index(request):
    kurslar=Course.objects.all()
    kategoriler=Category.objects.all()
    return render(request,'courses/index.html',{
        'categories':kategoriler,
        'courses':kurslar

    })
def details(request,kurs_id):
    # try:
    #   course=Course.objects.get(pk=kurs_id)
    # except:
    #     raise Http404()
    course=get_object_or_404(Course,pk=kurs_id)
    context={
        "course":course
    }
    
    return render(request,'courses/details.html',context)

def getCoursesByCategory(request,category_name): 
    try:

       category_text=data[category_name];
       print(category_text)
       return render(request,"courses/kurslar.html",{
           'category':category_name,
           'category_text':category_text
       })  
    except Exception as e:
        return HttpResponseNotFound("yanlış kategori seçimi",e)

def getCoursesByCategoryId(request,category_id):
    category_list=list(data.keys())
    if(category_id > len(category_list)):
        return HttpResponseNotFound("yanlış kategori seçimi")
    category_name=category_list[category_id -1]
    redirect_url=reverse('courses_by_category',args=[category_name])


    return redirect(redirect_url)
