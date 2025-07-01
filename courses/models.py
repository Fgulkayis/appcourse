
from django.db import models
from django.utils.text import slugify

class Category(models.Model):
        name=models.CharField(max_length=40)
        slug=models.SlugField(default="",null=False,unique=True,db_index=True,  max_length=50)
        def __str__(self):
            return f"{self.name}"
        
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    imageUrl=models.CharField(max_length=50, blank=False)
    date = models.DateField(auto_now_add=True)
    isActive = models.BooleanField(default=True)
    slug=models.SlugField(default="",blank=True,null=False,unique=True,db_index=True)
    category=models.ForeignKey(Category,default=1,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.title} {self.date}"
     
