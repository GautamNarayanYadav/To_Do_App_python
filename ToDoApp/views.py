from django.shortcuts import render,redirect
from .models import NewTask
def saveinfo(request):
    if request.method == "POST":
        AddTask=request.POST['addtask']
        time=request.POST['time']
        add=NewTask(AddTask=AddTask,time=time)
        add.save()
    Add = NewTask.objects.all()
    return render(request,"index.html",{'Add':Add})
def index(request):
    Add = NewTask.objects.all()
    return render(request,"index.html",{'Add':Add})
def Delete(request,id):
        New = NewTask.objects.get(id=id)
        New.delete()
        return redirect('/')

def about(request):
    return render(request, "about.html")       