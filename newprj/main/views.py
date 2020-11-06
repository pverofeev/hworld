from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')



#def forum(request):
 #   return HttpResponse("<h4>forum<h4>")
