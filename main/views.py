# Create your views here.
from django.shortcuts import render
from .models import *

def aboutipssm(request): 
    return render(request,'aboutippsm.html')

def index(request): 
    if request.method == "POST":
        
        if 'name' in request.POST:
            name = request.POST['name'] 
            gmail = request.POST['gmail'] 
            mobile = request.POST['mobile'] 
            place = request.POST['place']
            course = request.POST['Course'] 
            Enquiry.objects.create(name=name,email=gmail,phone=mobile,place=place,course=course)
        elif 'email' in request.POST:
            email = request.POST['email']
            Newsletter.objects.create(email=email)
            return render(request,'index.html')
        
    testmonial = testmonials.objects.all()
    context = {
        'testmonial':testmonial
    }
    
    return render(request,'index.html',context)


def aboutsrinivas(request): 
    if request.method == "POST":
        email = request.POST['email']
        Newsletter.objects.create(email=email)

        return render(request,'About-Srinivas University.html')
    return render(request,'About-Srinivas University.html')

def logistics(request): 
    if request.method == "POST":
        email = request.POST['email']
        Newsletter.objects.create(email=email)
    return render(request,'BBA - Logistics and Supply Chain Management.html')

def port(request): 
    if request.method == "POST":
        email = request.POST['email']
        Newsletter.objects.create(email=email)
    return render(request,'BBA - Port Shipping Management and Logistics.html')

def mba(request): 
    if request.method == "POST":
        email = request.POST['email']
        Newsletter.objects.create(email=email)
    return render(request,'MBA - Logistics and Supply chain Management.html')

def contact(request): 
    if request.method == "POST":
        email = request.POST['email']
        Newsletter.objects.create(email=email)
    return render(request,'contact.html')

def events(request): 
    if request.method == "POST":
        email = request.POST['email']
        Newsletter.objects.create(email=email)
        return render(request,'events.html',context)

    allevent = Event.objects.all()
    context={
        'event':allevent
    }
    return render(request,'events.html',context)

def eventview(request,pk):
    if request.method == "POST":
        email = request.POST['email']
        Newsletter.objects.create(email=email)
        return render(request,'eventdetails.html',context)


    eventdetails = Event.objects.filter(slug=pk)
    context = {
        'event':eventdetails
    }
    return render(request,'eventdetails.html',context)

def faculty(request): 
    if request.method == "POST":
        email = request.POST['email']
        Newsletter.objects.create(email=email)
        return render(request,'faculty.html',context)

    allfacuty = Faculty.objects.all()
    context = {
        'faculty':allfacuty
    }
    return render(request,'faculty.html',context)

def gallery(request):
    if request.method == "POST":
        email = request.POST['email']
        Newsletter.objects.create(email=email)
        return render(request,'gallery.html',context)
    
    galleryimages = Gallery.objects.all() 
    context = {
        'gallery':galleryimages
    }
    return render(request,'gallery.html',context)

def placement(request): 
    if request.method == "POST":
        email = request.POST['email']
        Newsletter.objects.create(email=email)
        return render(request,'placement.html')
    allplacements = placements.objects.all()
    context = {
        "placements": allplacements
    }
    return render(request,'placement.html',context)

def stdach(request):
    if request.method == "POST":
        email = request.POST['email']
        Newsletter.objects.create(email=email)
        return render(request,'student-achivements.html')
    student = studentachi.objects.all()
    context = {
        'student':student
    }
    return render(request,'student-achivements.html',context)
    
def tchach(request):
    if request.method == "POST":
        email = request.POST['email']
        Newsletter.objects.create(email=email)
        return render(request,'teacher-achivements.html')
    teacher = teacherachi.objects.all()
    context = {
        'teacher':teacher
    }
    return render(request,'teacher-achivements.html',context)
    

