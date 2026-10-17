
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm


def home(request):
    search = request.GET.get('department', '')

    employees = Employee.objects.all()

    if search:
        employees = employees.filter(department__icontains=search)

    return render(request, 'home.html', {
        'employees': employees,
        'total': employees.count(),
        'search': search
    })


def add_employee(request):
    form = EmployeeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'add_emp.html', {'form': form})


def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        employee.delete()

    return redirect('home')


def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    form = EmployeeForm(request.POST or None, instance=employee)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'edit.html', {'form': form})
