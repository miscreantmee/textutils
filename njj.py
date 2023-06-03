#i have created this
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>NJ</h1> <p1> hie how uh doing</p1>")
def about(request):
    return HttpResponse("hello Nancy")
def ws(request):
    return HttpResponse("<h1>NJ</h1> <p1> hie how uh doing</p1> <a href='https://hackernoon.com/data-inspired-5c78db3999b2'> data driven</a>>")