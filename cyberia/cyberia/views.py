from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def accountinfo(request):
    try:
        u = User.objects.get(username='default')
        u.objects.set(interests='so many coisas')
        userinterests = u.Member.interests
        print(userinterests)
    except:
        print('Not logged in.')
    return render(request, 'accountinfo.html')

def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')

    else:
        f = UserCreationForm()

    return render(request, 'registration/register.html', {'form': f})