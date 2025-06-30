from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request,'pages/contact.html')
def about(request):
    return render(request,'pages/about.html')
def index(request):
    return render(request,'pages/index.html')
