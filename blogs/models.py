from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class category (models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    created_at =  models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'categories'
    

    def __str__(self):
        return self.category_name
    
STATUS_CHOICES = (
    ('Draft','Draft'),
    ('Published','Published')

)    

class Blog(models.Model):
      
    title = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    category = models.ForeignKey (category,on_delete=models.CASCADE)
    authory =  models.ForeignKey (User,on_delete=models.CASCADE)
    feature_image = models.ImageField (upload_to='uploads%Y%m%d')
    short_description = models.TextField(max_length=500)
    blog_body =  models.TextField(max_length=2000)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Draft')
    is_featured =   models.BooleanField (default=False)
    created_at =  models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # string representation of model blog
    def __str__ (self):
        return self.title

       
    