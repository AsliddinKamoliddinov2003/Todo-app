from django import forms
from main.forms import CreatePostForm
from .models import *
from django.shortcuts import redirect, render
from django.urls import reverse


def index(request):
    data = Information.objects.all()

    context = {
        "data": data
    }

    return render(request, "index.html", context)



def post_detail(request, pk):
    new = Information.objects.filter(id=pk)

    if not new.exclude():
        return redirect(reverse("index"))
    else:
        new = new.first()

    context = {
        "new":new
    }

    return render(request, "post_detail.html", context)


def create_post(request):
    form = CreatePostForm

    if request.method == "POST":
        form  =  CreatePostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("index"))

    context = {
        "form":form
    }

    return render(request, "create_post.html", context)


def update_post(request, pk):
    new = Information.objects.filter(id=pk)
    
    if not new.exclude():
        return redirect(reverse("index"))
    else:
        new = new.first()

    form = CreatePostForm(instance=new)

    if request.method == "POST":
        new = CreatePostForm(request.POST, instance=new)
        if new.is_valid():
            new.save()
            return redirect(reverse("index"))

    context = {
        "form":form
    }

    return render(request, "update_post.html", context)


def delete_post(request, pk):
    try:
        new = Information.objects.filter(id=pk)
        new.delete()
    except Information.DoesNotExist:
        pass

    return redirect(reverse("index"))
    

