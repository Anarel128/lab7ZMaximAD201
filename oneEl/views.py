from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from .forms import AddOwn, FormForMod
#from modurapp import parc



def createor(request):
    if request.method == "POST":
        ord = Own()
        ord.name = request.POST.get("name")
        ord.package = request.POST.get("package")
        ord.modelgaika = request.POST.get("modelgaika")
        ord.telef = request.POST.get("telef")
        ord.addres = request.POST.get("addres")
        ord.save()
        return HttpResponseRedirect("/")
    else:
        AddForm = AddOwn()
        return render(request, "createor.html", {"form": AddForm})

def orders(request):
    ord = Own.objects.all()
    return render(request, "orders.html", {"ord": ord})

def mainpage(request):
    if request.method == "POST":
        FormFor = FormForMod()
        url = request.POST.get("link")
        n = request.POST.get("number")
        l = parc(url,n)
        return render(request, "mainpage.html", {"par": l,"form": FormFor})
    else:
        FormFor = FormForMod()
        return render(request, "mainpage.html", {"par": ["none"],"form": FormFor})
    #return render(request, "mainpage.html")


import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def parc(url, n):
    headers = {"User-Agent":UserAgent().random}
    urlf = url
    response = requests.get(urlf, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    data = soup.find_all("tr", {"class": "wrap"})
    main_l = []
    m = int(n)
    b = 0
    for data in data:
        if b < m:
            name = data.find("strong").text.replace("\n","")
            main_l.append(name)
            b+=1


    return main_l
