from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . forms import admin
# from . models import user


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        email = request.POST['email']
        print(pass1)
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('signup')

        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already taken.')
            return redirect('signup')
        new_user = User.objects.create(
            username=username, email=email)
        new_user.set_password(pass1)
        new_user.save()
        messages.success(
            request, "Your Account has been successfully created.")
        return redirect('home')
    return render(request, 'signup.html')


def signin(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
     
        user = authenticate(username=username,password=pass1)
        print(user)
        if user is not None:
            login(request,user)
            request.session['username'] = username
            if request.user.is_superuser:
                    return redirect('add')
            else:
                   return redirect('home')
            

        else:
            messages.error(
                request, 'Invalid username or password. Please try again.')
            return redirect("signin1")
    return render(request, 'signin.html')

@login_required(login_url='signin1')
def home(request):
    return render(request, "index.html")


@login_required(login_url='signin1')
def signout(request):
    logout(request)

    return redirect('signup')


def add(request):
    if request.method == 'POST':
        fm = admin(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['username']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(username=nm, email=em, password=pw)

            reg.save()
            fm = admin()
    else:
        fm = admin()
    adm =User.objects.all()
    return render(request,'add.html', {'form': fm, 'ad': adm})


def update(request, id):

    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = admin(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('add')
    else:
        pi = User.objects.get(pk=id)
        fm = admin(instance=pi)

        return render(request, 'update.html', {'fm': fm, 'pi': pi})


def delete(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/add')
