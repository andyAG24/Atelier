from django.shortcuts import render
from .models import Employee, EmployeeServices
from Service.models import Service

def all_employees(request):
    context = {}
    context['user_group'] = request.user.groups.all()[0].name

    employees_list = []
    for employee in get_employees():
        employees_list.append({
            'employee_object': employee,
            'employee_services': get_employee_services(employee)
        })
    context['employees'] = employees_list
    return render(request, 'employee/all_employees.html', context)

def get_employees():
    employees = Employee.objects.all()
    return employees

def get_employee_services(employee):
    employee_user_profile = employee.id
    employee_services = EmployeeServices.objects.filter(id_employee=employee_user_profile.id)

    services_list = []
    for employee_service in employee_services:
        service = Service.objects.get(id=employee_service.id_service.id)
        services_list.append(service)
    return services_list

def view_employee(request, id):
    context = {}
    context['user_group'] = request.user.groups.all()[0].name

    employee = Employee.objects.get(id=id)
    context['employee'] = employee
    context['employee_services'] = get_employee_services(employee)

    return render(request, 'employee/view_employee.html', context)
