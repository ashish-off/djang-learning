from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("<h1>Welcome to Ashish's Django App <br> This is HomaPage</h1>")
    return render(request, 'website/index.html')

def about(request):
    # return HttpResponse("<h1>Welcome to Ashish's Django App <br> This is AboutPage</h1>")
    return render(request , 'about.html')

def contact(request):
    # return HttpResponse("<h1>Welcome to Ashish's Django App <br> This is ContactPage</h1>")
    return render(request, 'contact.html')