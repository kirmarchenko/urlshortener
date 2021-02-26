from django.db import IntegrityError
from django.shortcuts import render, redirect


from .forms import URLForm
from .models import Shortened


def index(request):
    # резервируем имя переменной на случай ошибки
    error = ''
    if request.method == "POST":
        # здесь и дальше готовим данные из формы,
        # т.к. нам пришел POST запрос
        form = URLForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_url = Shortened(**data)
            try:
                # пробуем сохранить ссылки в БД
                new_url.save()
                # и отправить пользователя на страницу с результатом
                return render(request, 'shortener/success.html', {'urls': form.cleaned_data})
            except IntegrityError:
                # если поймали IntegrityError - регистрируем ошибку
                error = data['shortened']
    else:
        # если же это запрос первый раз, то создаем пустую форму
        form = URLForm()
    # и показываем главную страницу, с ошибкой или без
    return render(request, 'shortener/index.html', {'form': form, 'error': error})


def shortened(request, url):
    # ищем в БД полученную короткую ссылку, которая хранится
    # в переменной url. Находим объект с этой короткой ссылкой,
    # и извлекаем из него изначальную длинную
    initial_url = Shortened.objects.get(shortened=url).initial_url
    # по этой длинной ссылке и перенаправляем пользователя
    return redirect(initial_url)

