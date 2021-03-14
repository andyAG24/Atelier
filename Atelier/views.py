from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def mainpage_view(request):
    context = {}

    return render(request, 'main.html')
