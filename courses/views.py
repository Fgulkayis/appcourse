from datetime import date,datetime
from django.shortcuts import get_object_or_404, render
from .models import Course,Category
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.


def index(request):
    kurslar=Course.objects.all()
    kategoriler=Category.objects.all()

    paginator = Paginator(kurslar, 2)  # Her sayfada 2 kurs
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'courses/index.html',{
        'categories':kategoriler,
        'page_obj':page_obj

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
    return render(request,'courses/index.html', {
        'categories':kategoriler,
        'page_obj':page_obj,
        'seciliKategori':slug
    })