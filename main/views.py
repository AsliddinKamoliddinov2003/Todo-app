from .models import *
from django.shortcuts import redirect, render
from django.urls import reverse



def index(request):
    if request.method=='POST':
        work=request.POST['work']
        new=Information(description=work)
        new.save()

    news=Information.objects.all()
    context = {
        "news":news
    }
    return render(request, "todo.html", context)


def finishtodo(request,pk):
    Information.objects.filter(id=pk).update(status='True')
    return redirect(reverse("index"))


def davometish(request, pk):
    Information.objects.filter(id=pk).update(status='False')
    return redirect(reverse("index"))


def delete(request, pk):
    try:
        work = Information.objects.get(id=pk)
        work.delete()
    except Information.DoesNotExist():
        pass

    return redirect(reverse("index"))


def update(request, pk):
    if request.method=='POST':
        work=request.POST['work']
        Information.objects.filter(id=pk).update(description=work)
        return redirect(reverse("index"))

    work=Information.objects.get(id=pk)
    context = {
        "work":work
    }
    return render(request,'update.html', context)




