from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Transpose',
        'style': 'transpose.css',
        'script': 'transpose.js'
    }
    return render(request, 'transpose/index.html', context)