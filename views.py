from django.http import HttpResponse
from django.shortcuts import render
from.models import CONTACT
def home(request):
    return render(request,'app/home.html')
def contact(request):
    if request.method=="POST":
        CONTACT = CONTACT()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=subject.POST.get('subject')
        message=message.POST.get('message')
        CONTACT.name=name
        CONTACT.email=email
        CONTACT.subject=subject
        CONTACT.message=message
        CONTACT.save()
        return HttpResponse("Your Message Submitted Successfully")

    return render(request,'app/contact.html')
def about(request):
    return render(request,'app/about.html')
def courses(request):
    return render(request,'app/courses.html')
def c(request):
    return render(request,'app/c.html')
def HTML(request):
    return render(request,'app/HTML.html')
def java(request):
    return render(request,'app/java.html')
def python(request):
    return render(request,'app/python.html')
def Css(request):
    return render(request,'app/Css.html')



# Create your views here.
