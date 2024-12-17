from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import UserRegister
from django.core.paginator import Paginator



def home(request):
    title = 'Game 365'
    context = {'title': title}
    return render(request, 'home.html', context)

def game(request):
    games = Game.objects.all()
    title = 'Game 365'
    print(games)
    context = {
        'games': games,
        'title': title,
    }
    return render(request, 'game.html', context)

def basket(request):
    title = 'Game 365'
    return render(request, 'basket.html',
                  {'title': title})

def rega(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            Buyer.objects.create(username=f"{username}", age=age)
            return HttpResponse(f'Приветствуем {username}')
    else:
        form = UserRegister()
    return render(request, 'rega.html', {'form': form})

def news(request):
    news = News.objects.all().order_by('date')
    paginator = Paginator(news, 3)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(request, 'news.html', {'page_obj': page_obj})
