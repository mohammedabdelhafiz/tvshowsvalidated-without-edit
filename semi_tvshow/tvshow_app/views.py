from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from . import models


def index(request):
 
    return render(request,"basic.html")



def addshow(request):
    shows=request.POST
    result=models.add_show(shows['title'],shows['network'],shows['releasedate'],shows['description'])
    return redirect('/showtwo/'+str(result.id))

def showtwo(request,id):
    context={
        'show':models.get_showbyid(id)
        
    }
    return render(request,'show.html',context)

def shows(request):
    context={
        'shows':models.get_all_shows()
    }
    return render(request,'template.html',context)

def delete(request,id):
        models.delete_show(id)
        return redirect('/shows')

def edit(request,id):
        models.get_showbyid(id)
        shows.title=request.POST['title']
        shows.network=request.POST['network']
        shows.releasedate=request.POST['releasedate']
        shows.description=request.POST['description']
        shows.sa
        return render(request,"edit_sh.html")

    