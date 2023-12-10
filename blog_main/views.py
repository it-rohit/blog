from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import category,Blog
from assignment.models import About_1
from assignment.models import Social_link

def home (request):
    # category_details=category.objects.all()
    feature_post = Blog.objects.filter(is_featured=True,status='Published').order_by('update_at')
    post = Blog.objects.filter(is_featured=False,status='Published')

    # Social_link1 = Social_link.objects.all()


    # fetch about us
    try:
        about = About_1.objects.get()
    except:
        about = None

    context = {
        # 'category':category_details,
        'feature_post' :feature_post,
        'post' : post,
        'about': about,
        # for it work in views but not works in context manager
        # 'socal': Social_link1
    }
    return render(request,'home.html',context)
