from django.shortcuts import render, HttpResponse
from .models import Student

# Create your views here.
def iStore_homepage(request):
    return render(request, 'index.html')

def new_student(request, name, em):
    print(name, em, 77777)
    Student.objects.create(name=name, emailid=em)
    return HttpResponse("Student Added")

def all_students(request):
    all_studs = Student.objects.all()
    data = [ (i.name, i.emailid) for i in all_studs ]
    return HttpResponse(data)

def update_student(request, name, new_em):
    stud = Student.objects.get(name=name)
    stud.emailid = new_em
    stud.save()
    return HttpResponse('Updated')

def delete_student(request, name):
    stud = Student.objects.get(name=name)
    stud.delete()
    return HttpResponse('Deleted')

