from django.contrib.auth.decorators import login_required,user_passes_test
from django.shortcuts import get_object_or_404, redirect,render
from courses.forms import CourseCreateForm, CourseEditForm, uploadForm
from .models import Course,Category, uploadModel
from django.core.paginator import Paginator

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

def isAdmin(user):
   return user.is_superuser

@user_passes_test(isAdmin)
def create_course(request):
    
    if request.method == "POST":
     form= CourseCreateForm(request.POST, request.FILES)

     if form.is_valid():
        form.save()
        return redirect("/kurslar")
    else:
     form = CourseCreateForm()     
    return render(request,"courses/create-course.html",{"form":form})

@login_required()
def course_list(request):
    kurslar=Course.objects.all()
    return render(request,'courses/course-list.html',{
        'courses':kurslar
    })

def course_edit(request,id):
   course= get_object_or_404(Course,pk=id)
 
   if request.method == "POST":
      form= CourseEditForm(request.POST, request.FILES,instance=course)
      form.save()
      return redirect("course_list")
   else:
      form=CourseEditForm(instance=course)

   return render(request, "courses/edit-course.html",{ "form":form ,"course":course})

def course_delete(request,id):
   course= get_object_or_404(Course,pk=id)

   if request.method ==  "POST":
     course.delete()
     return redirect("course_list")
   return render(request,"courses/course-delete.html",{'course':course})


def upload(request):
   if request.method == "POST":
      form = uploadForm(request.POST,request.FILES)

      if form.is_valid():
        
        model= uploadModel(image=request.FILES["image"])
        model.save()
        return render(request, "courses/success.html")
   else:
      form=uploadForm()
   return render(request,"courses/upload.html",{"form":form})
   

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