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
def details(request,slug):
    # try:
    #   course=Course.objects.get(pk=kurs_id)
    # except:
    #     raise Http404()
    course=get_object_or_404(Course,slug=slug)
    context={
        "course":course
    }
    
    return render(request,'courses/details.html',context)

def getCoursesByCategory(request,slug):
    kurslar=Course.objects.filter(category__slug=slug, isActive=True)
    kategoriler=Category.objects.all()
    
    return render(request,'courses/index.html',{
        'categories':kategoriler,
        'courses':kurslar,
        'seciliKategori':slug
    })
