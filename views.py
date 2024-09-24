from django.shortcuts import render
from django.http import HttpResponse
from task5.forms import *

# Create your views here.

users = ['Vasy', 'Pety', 'Sasha', 'Galy', 'Vally', 'Trevor', 'Mikle', 'Franklin', 'SUPER_MEGA_POWER_DRISH']

def registration_html(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        age = request.POST.get('age')
        print('-----------------------------------')
        print(f'Name:{name}')
        print(f'Age:{age}')
        print('-----------------------------------')
        for i in users:
            if i == name:
                error = 'Такой пользователь уже есть!'
                return render(request, 'registration_page.html', {'error': error})
        if int(age) < 18:
            error = 'Возраст должен быть больше 18!'
            return render(request, 'registration_page.html', {'error': error})
        if password_1 != password_2:
            error = 'Пароли не совпадают!'
            return render(request, 'registration_page.html', {'error': error})
        else:
            return HttpResponse(f'Приветствуем {name}')
    return render(request, 'registration_page.html', {'error': None})


def registration_django(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password_1 = form.cleaned_data['password_1']
            password_2 = form.cleaned_data['password_2']
            age = form.cleaned_data['age']
            print('-----------------------------------')
            print(f'Name:{name}')
            print(f'Age:{age}')
            print('-----------------------------------')
            for i in users:
                if i == name:
                    error = 'Такой пользователь уже есть!'
                    return render(request, 'registration_page.html', {'error': error})
            if password_1 != password_2:
                error = 'Пароли не совпадают!'
                return render(request, 'registration_page.html', {'error': error})
            if int(age) < 18:
                error = 'Возраст должен быть больше 18!'
                return render(request, 'registration_page.html', {'error': error})
    else:
        form = RegForm()
    return HttpResponse(f'Приветствуем {name}')