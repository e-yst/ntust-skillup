from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from main.forms import SignupForm, LoginForm
from main.models import Member

from datetime import datetime
from pytz import timezone as tz
# Create your views here.


def signup(request):
    if request.method == 'GET':
        form = SignupForm.SignupForm()
        context = {'form': form}
        return render(request, 'signup.html', context)
    elif request.method == 'POST':
        form = SignupForm.SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['name']
            password = form.cleaned_data['password']
            mail = form.cleaned_data['mail']
            user_bio = form.cleaned_data['user_bio']

            dob = datetime.strptime(
                form.cleaned_data['dob'],
                '%Y/%m/%d'
            ).replace(tzinfo=tz('Asia/Taipei'))

            gender = m_or_f(form.cleaned_data['gender'])

            u = User.objects.create(username=username,
                                    password=password,
                                    email=mail)

            Member.objects.create(user=u,
                                  gender=gender,
                                  dob=dob,
                                  user_bio=user_bio)

            return redirect('login')
        else:
            print(form.errors)
            context = {'form': form}
            return render(request, 'signup.html', context)


def signin(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'GET':
        form = LoginForm.LoginForm()
        context = {'form': form}
        return render(request, 'login.html', context)
    elif request.method == 'POST':
        form = LoginForm.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['name']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            login(request, user)
            context = {'form': form}
            return redirect('index')

        else:
            context = {'form': form}
            return render(request, 'login', context)


@login_required
def signout(request):
    logout(request)
    return redirect('index')


def m_or_f(txt):
    return False if txt == "0" else True
