from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Blog,category   
from django.db.models import Q


# Create your views here.
def posts_by_category(request,category_id):
    print(category_id)
    # fetch post by category by using cateogry_id
    post = Blog.objects.filter(status ='Published',category_id = category_id  )
    # print(post)
    # in blog models the forgien key always store in tems of id ie refer table
    # try:
    #     category_name = category.objects.get(pk=category_id)
    #     # print(category)
    # except:
    #     pass
    # this can be done in single line
    category_name = get_object_or_404(category, pk=category_id)
        
    context = {
        'post' : post ,
        'category_name' : category_name,

    }
    return render (request,'posts_by_category.html',context)


def blogs (request,slug):
    single_blog = get_object_or_404(Blog, slug=slug, status= 'Published' )
    context = {
        'single_blog' : single_blog
    }

    return render (request,'blogs.html',context)

def search (request):
    keyword = request.GET.get('keyword')
    # print('keywrd==>',keyword)
    blogs = Blog.objects.filter(Q (title__icontains=keyword) | Q(short_description__icontains = keyword  )| Q(blog_body__icontains = keyword  ), status="Published" )
    # print (blogs)
    context = {
        'blogs':blogs,
        'keyword':keyword

    }
    return render(request,'search.html',context)

