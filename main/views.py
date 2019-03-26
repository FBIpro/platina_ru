from django.shortcuts import render
from main.models import News

# Create your views here.

def home(request):
    newses = News.objects.all()
    #импортнули данные загруженные с админки
    return render(request, "main/home.html", {"newses": newses})

def about(request):
    return render(request, "main/about.html")

def services(request):
    return render(request, "main/services.html")

def contact(request):
    return render(request, "main/contact.html")

def news(request):
    return render(request, "main/news.html")
