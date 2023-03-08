from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'data/home.html')

def about(request):
    return render(request, 'data/about.html')

def contact(request):
    return render(request, 'data/contact.html')

def pricing(request):
    return render(request, 'data/pricing.html')
