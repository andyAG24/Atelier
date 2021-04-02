from django.shortcuts import render

def render_menu(request):
    print()
    return render(request, 'templates/header.html', {'values': ['группа1', 'группа2']})
