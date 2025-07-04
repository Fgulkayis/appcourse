from datetime import date,datetime
from django.shortcuts import get_object_or_404, redirect,render
from courses.forms import CourseCreateForm
from .models import Course,Category
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here. 
def search(request):
    #print(request.GET) talebin içindeki bilgiyi  servera yazdırırkurslar=Course.objects.all()
    if "q" in request.GET and request.GET["q"] != "" :
       q=request.GET["q"]
       kurslar=Course.objects.filter(isActive=True,title__contains=q).order_by("date")
       kategoriler=Category.objects.all()

    else:
        return redirect("/kurslar")
    
    return render(request,'courses/search.html', {
        'categories':kategoriler,
        'courses':kurslar
        
    })
def create_course(request):
    if request.method == "POST":
     form= CourseCreateForm(request.POST)

     if form.is_valid():
        form.save()
        return redirect("/kurslar")
    else:
     form = CourseCreateForm()     
    return render(request,"courses/create-course.html",{"form":form})

def index(request):
    kurslar=Course.objects.filter(isActive=1,isHome=1)
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
    kurslar=Course.objects.filter(categories__slug=slug, isActive=True).order_by("date")
    kategoriler=Category.objects.all()


    paginator=Paginator(kurslar,2)
    page_number=request.GET.get('page') 
    
    page_obj = paginator.get_page(page_number)
    return render(request,'courses/list.html', {
        'categories':kategoriler,
        'page_obj':page_obj,
        'seciliKategori':slug
    })