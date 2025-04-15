from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):
    # feature1 = Feature(0, 'Fast', 'Our service is very quick')
    # feature2 = Feature(1, 'Secure', 'Your data is safe with us')
    # feature3 = Feature(2, 'Reliable', 'Runs 24/7 without issues')
    # feature4 = Feature(3, 'Affordable', 'Cost-effective for everyone')

    # features = [feature1, feature2, feature3, feature4]

    features = Feature.objects.all()

    context = {
        'name': 'Kshitij',
        'age': 19,
        'nationality': 'Indian',
        'features': features  
    }

    # return render(request, 'index.html', context)
    return render(request, 'index.html', {'features': features})



def register(request):
    if request.method == 'POST': 
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2: 
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already used')
                return redirect(register)
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'User name already used')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save(); 
                return redirect('login')
        else:
            messages.info(request, 'Password not the same')
            return redirect('register')
    else:
        return render(request, 'register.html')
    

def Login(request):
    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password= password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')
    

def Logout(request):
    auth.logout(request)
    return redirect('/')

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})


def post(request, pk):
    return render(request, 'post.html', {'pk':pk})

