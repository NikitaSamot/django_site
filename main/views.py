from django.shortcuts import render
from goods.models import Categories
# Create your views here.
def index(request):
    categories = Categories.objects.all()
    
    context = {
        'text_h1': 'Мага мебели',
        'categories': categories
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'text_about': 'Страница о нас'
    }
    return render(request, 'main/about.html', context)