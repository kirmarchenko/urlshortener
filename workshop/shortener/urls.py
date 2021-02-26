from django.urls import path

from . import views

# Здесь описываем с какими ссылками будет работать наше приложение
urlpatterns = [
    # если ссылка пустая (http://127.0.0.1:8000/) - показываем главную
    path('', views.index, name='index'),
    # а если в адресе есть строка (http://127.0.0.1:8000/short_url)
    # то обрабатываем ее как короткую ссылку, помещая в переменную "url"
    path('<str:url>', views.shortened, name='shortened')
]
