from django.shortcuts import render
from .forms import SignupForm

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
        return render(request, 'signup.html', context)
