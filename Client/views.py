from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Client

@login_required(login_url='auth')
def all_clients(request):
    context = {}
    context['user_group'] = request.user.groups.all()[0].name

    context['clients'] = Client.objects.all()
    return render(request, 'client/all_clients.html', context)

def view_client(request, id):
    context = {}
    context['user_group'] = request.user.groups.all()[0].name

    client_object = Client.objects.get(id=id)
    context['client'] = {
        'client_object': client_object
    }
    return render(request, 'client/view_client.html', context)
    