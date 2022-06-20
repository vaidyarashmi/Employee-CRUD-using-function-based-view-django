from django.shortcuts import render,redirect
from testapp.models import Employee
from testapp.forms import EmployeeForm
# Create your views here.
def show_view(request):
    employee=Employee.objects.all()
    return render(request,'index.html',{'employee':employee})

def insert_view(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/show_view')
    return render(request,'insert.html',{'form':form})

def update_view(request,id):
    emp=Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
        return redirect('/show_view')
    return render(request,'update.html',{'emp':emp})

def delete_view(request,id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return redirect('/show_view')