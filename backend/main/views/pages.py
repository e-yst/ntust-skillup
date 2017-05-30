from django.shortcuts import render
from main.models import Category, Lesson


def index(request):
    if request.user.is_authenticated:
        context = {
            'username': request.user.username,
            'categories': Category.objects.all(),
        }
        return render(request, 'index.html', context)
    else:
        context = {
            'categories': Category.objects.all(),
        }
        return render(request, 'index.html', context)


def details(request, id):
    l = Lesson.objects.get(id=id)
    l.click_counter += 1
    l.save()
    context = {'lesson': l}
    return render(request, 'details.html', context)


def categories(request, name):
    c = Category.objects.get(name=name)
    context = {'category': c}
    return render(request, 'categories.html', context)
