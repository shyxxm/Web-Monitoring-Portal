from tokenize import String
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Website
import pip._vendor.requests
from urllib.request import urlopen
import time
import json
from .forms import UrlForm


# Create your views here.

# def home(request):
#     return render(request,'monitor/home.html',{})

# def home(request):
#     webs = Website.objects.values()

#     godss = webs
#     lst=[]
#     for god in godss:
#         webbie = god['website']
#         request_response = pip._vendor.requests.head(webbie)
#         status_code = request_response.status_code
        
#         website_is_up = status_code == 200
#         lst.append(website_is_up)
#         print(website_is_up)
#         print(god['website'])
#     json_list = json.dumps(lst)
#     print(json_list)
#     print(webs)

#     return render(request,'monitor/home.html',{'webs':webs,'json_list':json_list})

def home(request):
    webs = Website.objects.values()
    godss = webs
    webs_list = []
    for god in godss:
        item = {
            "url": god,
            "status": False
        }

        webbie = god['website']
        request_response = pip._vendor.requests.head(webbie)
        status_code = request_response.status_code

        website_is_up = status_code == 200
        print(website_is_up)

        if website_is_up is True:
            item["status"] = "True"
            webs_list.append(item)
        else:
            item["status"] = "False"
            webs_list.append(item) 
    print(webs_list)  
    return render(request, 'monitor/home.html', {'webs_list': webs_list})

def add_url(request):
    webs = Website.objects.values()
    godss = webs
    webs_list = []
    for god in godss:
        item = {
            "url": god,
            "status": False
        }

        webbie = god['website']
        request_response = pip._vendor.requests.head(webbie)
        status_code = request_response.status_code
        
        website_is_up = status_code == 200
        print(website_is_up)

        if website_is_up is True:
            item["status"] = "True"
            webs_list.append(item)
        else:
            item["status"] = "False"
            webs_list.append(item) 
    print(webs_list) 
    submitted = False
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_url?submitted=True')
    else:
        form = UrlForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request,'monitor/add_url.html',{'webs_list': webs_list,'form':form,'submitted':submitted})

def search_url(request):
    if request.method == "POST":
        searched = request.POST['searched']
        print(searched)
        urls = Website.objects.filter(website__contains=searched).values()
        print(urls)
        godss = urls
        demo = []
        demo_list = {
            'header' : searched
        }
        demo.append(demo_list)
        print(demo_list)
        webs_list = []
        for god in godss:
            item = {
            "url": god,
            "status": False
        }

            webbie = god['website']
            request_response = pip._vendor.requests.head(webbie)
            status_code = request_response.status_code

            website_is_up = status_code == 200
            print(website_is_up)

            if website_is_up is True:
                item["status"] = "True"
                webs_list.append(item)
            else:
                item["status"] = "False"
                webs_list.append(item) 
        print(webs_list) 
        return render(request,'monitor/search_url.html',{'searched':searched,'webs_list':webs_list,'demo':demo})
    else:
        return render(request,'monitor/search_url.html',{})

def update_url(request,web):
    # print("Testing function")
    # return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")

    webid = Website.objects.get(pk=web)
    form = UrlForm(request.POST or None)
    #return render(request, 'monitor/home.html', {'webid': webid})
    return redirect('home',{'form':form})

def delete_url(request,web):
    url = Website.objects.get(pk=web)
    print(url)
    url.delete()
    return redirect('home')
        