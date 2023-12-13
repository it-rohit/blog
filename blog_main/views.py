from django.http import HttpResponse
from django.shortcuts import render,redirect
from blogs.models import category,Blog
from assignment.models import About_1
from assignment.models import Social_link
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


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

def register(request):
    if request.method == "POST":
        form = RegistrationForm (request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = RegistrationForm
        context = {
            'form': form,
        }
    return render (request,'register.html',context)

def login (request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username = username, password = password)
            if user is not None:
                auth.login(request, user)
            return redirect ("home")
        
    form = AuthenticationForm()
    context = {
        'form':form
    }
    return render (request, "login.html",context)

def  logout(request):
    auth.logout(request)
    return redirect ('home')