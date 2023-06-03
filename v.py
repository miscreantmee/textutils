# i have created this
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("home")


def removepunc(request):
    return HttpResponse("remove punctuations")


def capitalizefirst(request):
    return HttpResponse("captialize first letter")


def analyze(request):
    textdj = request.GET.get("Text", "default")
    anlyg = request.GET.get("anlyz", "off")
    print(textdj)
    print(anlyg)
    return HttpResponse("")


def newlineremove(request):
    return HttpResponse("remove newlines")


def charcount(request):
    return HttpResponse("count the characters")


def spaceremove(request):
    return HttpResponse("<p> removespace </p> <a href = '/'> back</a>")
