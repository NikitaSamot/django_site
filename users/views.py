from django.shortcuts import render

# Create your views here.
def login(request):
    context ={

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