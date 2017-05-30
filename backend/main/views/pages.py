from django.shortcuts import render


def index(request):
    if request.user.is_authenticated:
        print(request.user.username)
        context = {'username': request.user.username}
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')
