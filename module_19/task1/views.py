from django.shortcuts import render
from django.http import HttpResponse
from .models import Game, Buyer
from .forms import UserRegister



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
