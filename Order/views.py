from django.shortcuts import render

def kek(request):
    context = {}
    context['user_group'] = request.user.groups.all()[0].name
    return render(request, 'main.html', context)
