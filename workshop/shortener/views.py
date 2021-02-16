from django.db import IntegrityError
from django.shortcuts import render, redirect


from .forms import URLForm
from .models import Shortened


def index(request):
    error = ''
    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_url = Shortened(**data)
            try:
                new_url.save()
                return render(request, 'shortener/success.html', {'urls': form.cleaned_data})
            except IntegrityError:
                error = data['shortened']
    else:
        form = URLForm()
    return render(request, 'shortener/index.html', {'form': form, 'error': error})


def shortened(request, url):
    initial_url = Shortened.objects.get(shortened=url).initial_url
    return redirect(initial_url)

