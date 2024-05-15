from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse
from django.http import HttpResponseRedirect
from users.forms import UserLoginForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user :
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:home'))

    else:
       form = UserLoginForm()
       
    context ={
        'form': form
    }
    return render(request, 'users/login.html', context=context)

def registration(request):

    context ={

    }
    return render(request, 'users/registration.html', context=context)

def profile(request):
    context ={
    }
    return render(request, 'users/profile.html', context=context)

def logout(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context ={
        'product': product
    }
    return render(request, 'users/registration.html', context=context)