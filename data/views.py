from django.shortcuts import render
from .models import Image5, Image1, Image2, Image3, Image4, Image8,Image10,Image20,Image9

# Create your views here.

def home(request):
    image1=Image1.objects.all()
    image2=Image2.objects.all()
    image3=Image3.objects.all()
    image4=Image4.objects.all()
    image5=Image5.objects.all()
    image8=Image8.objects.all()
    image9=Image9.objects.all()
    image10=Image10.objects.all()

    context = {'image1': image1, 'image2': image2,'image3': image3,'image4': image4,'image5': image5,'image8': image8,'image9': image9,'image10': image10}
    return render(request, 'data/home.html', context)

def about(request):
    image20=Image20.objects.all()
    image1=Image1.objects.all()
    image8=Image8.objects.all()
    image10=Image10.objects.all()

    context={'image1': image1, 'image20':image20, 'image8': image8, 'image10': image10,}
    return render(request, 'data/about.html', context)

def contact(request):
    image1=Image1.objects.all()
    image8=Image8.objects.all()
    image10=Image10.objects.all()

    context={'image1': image1, 'image8': image8, 'image10': image10,}
    return render(request, 'data/contact.html', context)

def pricing(request):
    image1=Image1.objects.all()
    image8=Image8.objects.all()
    image10=Image10.objects.all()

    context={'image1': image1, 'image8': image8, 'image10': image10,}
    return render(request, 'data/pricing.html', context)
