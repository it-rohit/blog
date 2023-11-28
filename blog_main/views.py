from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import category,Blog

def home (request):
    # category_details=category.objects.all()
    feature_post = Blog.objects.filter(is_featured=True,status='Published').order_by('update_at')
    post = Blog.objects.filter(is_featured=False,status='Published')
    context = {
        # 'category':category_details,
        'feature_post' :feature_post,
        'post' : post
    }
    return render(request,'home.html',context)
