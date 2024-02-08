from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movie
from .forms import movieform
# Create your views here.
def movies(request):
    obj=movie.objects.all()
    context={
        'mov':obj
    }
    return render(request,'movie.html',context)
def detail(request,movie_id):
    obj1=movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'movi':obj1})
def add(request):
    if request.method=='POST':
        name=request.POST['name']
        desc=request.POST['desc']
        year=request.POST['year']
        img=request.FILES['img']
        mo=movie(name=name,desc=desc,year=year,img=img)
        mo.save();
        return redirect('/')
    return render(request,'add.html')
def update(request,id):
    movi=movie.objects.get(id=id)
    form=movieform(request.POST or None , request.FILES , instance=movi)
    if form.is_valid():
        form.save();
        return redirect('/')
    return render(request,'update.html',{'movi':movi,'form':form})
def delete(request,id):
    if request.method=='POST':
        mo=movie.objects.get(id=id)
        mo.delete();
        return redirect('/')
    return render(request,'delete.html')
