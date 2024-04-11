from django.shortcuts import render
from .models import MenuItem


def home(request):
    main_menu = MenuItem.objects.all()
    return render(
        request,
        'menu/menu.html',
        {'main_menu': main_menu}
    )
