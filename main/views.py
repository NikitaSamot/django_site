from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'hadame',
    }
    return render(request, 'main/index.html', context)