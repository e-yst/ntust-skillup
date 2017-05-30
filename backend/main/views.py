from django.shortcuts import render, redirect
from .forms import SignupForm
from .models import Member

from datetime import datetime
# Create your views here.

def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'GET':
        form = SignupForm()
        context = {'form': form}
        return render(request, 'signup.html', context)
    elif request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['name']
            password = form.cleaned_data['password']
            mail = form.cleaned_data['mail']
            gender = form.cleaned_data['gender']
            user_bio = form.cleaned_data['user_bio']
            dob = datetime.strptime(
                form.cleaned_data['dob'],
                '%Y/%m/%d'
            )

            Member.objects.create(username=username, password=password,
                                  email=mail, gender=gender,
                                  day_of_birth=day_of_birth, user_bio=user_bio)

            return redirect('index')
        else:
            print(form.errors)
            context = {'form': form}
            return render(request, 'signup.html', context)
