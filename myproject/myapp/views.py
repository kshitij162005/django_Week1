from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    # return HttpResponse('<h1> Hey Welcome </h1>')
    # name = 'Kshitij'
    context = {
        'name': 'Kshitij', 
        'age': 19, 
        'nationality': 'Indian'
    }
    return render(request, 'index.html', context)


def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})

# def features(request):
#     feature1 = Feature()
#     feature1.id = 0
#     feature1.name  = 'Fast'
#     feature1.details = 'Our service is very quick'

#     return render(request, 'index.html'), {'features':feature1 }