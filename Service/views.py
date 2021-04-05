from django.shortcuts import render
from .models import Service
from django.contrib.auth.decorators import login_required
from Employee.models import Employee, EmployeeServices
from ServicePrice.views import get_current_price, get_price_history

@login_required(login_url='auth')
def all_services(request):
    context = {}
    context['user_group'] = request.user.groups.all()[0].name
    
    services = Service.objects.all()
    services_list = []
    for service in services:
        employee_services = EmployeeServices.objects.filter(id_service=service.id)
        services_list.append({
            'service': service,
            'price': get_current_price(service.id),
            'employee_quantity': employee_services.__len__()
        })
    context['services'] = services_list

    return render(request, 'service/all_services.html', context)

@login_required(login_url='auth')
def view_service(request, id):
    context = {}
    context['user_group'] = request.user.groups.all()[0].name

    service = Service.objects.get(id=id)
    context['service'] = service
    context['service_prices'] = get_price_history(service.id)
    context['service_price'] = get_current_price(service.id)

    employee_service = EmployeeServices.objects.filter(id_service=id)
    
    employees = []
    for service in employee_service:
        employees.append(Employee.objects.get(user=service.id_employee))
    context['employees_in_service'] = employees
    return render(request, 'service/view_service.html', context)
