import imp
from django.shortcuts import render
from django.http import HttpResponse
from base.models import Url
from django.shortcuts import redirect

def createurl(request):
    if request.method=="POST":
        full_url=request.POST.get('full_url')
        obj=Url.create(full_url)
        return render(request,'base/index.html',{
            'full_url' :obj.full_url,
            'short_url': request.get_host()+'/'+obj.short_url
        })
    return render(request,'base/index.html')

def routetourl(request,key):
    try:
        obj=Url.objects.get(short_url=key)
        return redirect(obj.full_url)
    except:
        return redirect(createurl)

