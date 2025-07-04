
from django import forms
from courses.models import Course 

# class CourseCreateForm(forms.Form):
#     title = forms.CharField(
#         label="Kurs Başlığı",
#         required=True,
#         error_messages={"required":"kurs başlığı girmelisiniz."}, 
#         widget=forms.TextInput(attrs={"class":"form-control"}))
    
#     description = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
#     imageUrl=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     slug=forms.SlugField(widget=forms.TextInput(attrs={"class":"form-control"}))
class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title','description','imageUrl','slug',)
        labels = {
            'title':"Kurs Başlığı",
            'description':"Açıklama",
        }
        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control"}),
            "description": forms.Textarea(attrs={"class":"form-control"}),
            "imageUrl": forms.TextInput(attrs={"class":"form-control"}),
            "slug": forms.TextInput(attrs={"class":"form-control"}),
        }
        error_messages ={
            "title":{
                "required":"kurs başlığı girmelisiniz.",
                "max_length":"maksimum 50 karakter girmelisiniz"
            },
            "description":{
                "required":"kurs açıklaması gereklidir",
            }
        }