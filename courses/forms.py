from django import  forms 

class CourseCrateForm(forms.Form):
    title = forms.CharField()
    descriptiton = forms.CharField(widget=forms.Textarea)
    imageUrl=forms.CharField()
    slug=forms.CharField()
    