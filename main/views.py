from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'text_h1': 'Мага мебели'
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'text_about': 'Страница о нас'
    }
    return render(request, 'main/about.html', context)