from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from main.models import Category, Lesson


def index(request):
    lessons = Lesson.objects.all().order_by('-click_counter')[:15]
    categories = Category.objects.all()

    if request.user.is_authenticated:
        context = {
            'username': request.user.username,
            'categories': categories,
            'lessons': lessons,
        }
        return render(request, 'index.html', context)
    else:
        context = {
            'categories': categories,
            'lessons': lessons,
        }
        return render(request, 'index.html', context)


@login_required
def profile(request):
    context = {
        'username': request.user.username,
        'u': request.user,
    }
    return render(request, 'profile.html', context)


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
