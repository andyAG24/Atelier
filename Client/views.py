from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.utils.translation import ugettext_lazy as _
from Order.views import get_client_orders
from .forms import ClientForm
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
    context['orders'] = get_client_orders(id)
    return render(request, 'client/view_client.html', context)
    
def add_client(request):
    context = {}
    context['user_group'] = request.user.groups.all()[0].name

    error = ''
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_clients')
        else:
            error = _('Form is invalid')

    form = ClientForm()
    context['form'] = form
    context['error'] = error

    return render(request, 'client/add_client.html', context)

def delete_client(request, id):
    context = {}
    context['user_group'] = request.user.groups.all()[0].name

    Client.objects.filter(id=id).delete()
    return redirect('all_clients')

class EditClientView(UpdateView):
    model = Client
    template_name = 'client/add_client.html'
    form_class = ClientForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_group'] = self.request.user.groups.all()[0].name
        return context
