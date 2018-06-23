from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render_to_response
from  onlineapp.models import *
from django.db.models import Count
from django import template
# Create your views here.

def test_view(request):

    resp="<html><h1>worKING</h1></html>"
    return render_to_response(r'test.html ')
    #return"hello world"



def list_of_colleges(request):
    x=College.objects.values('name','acronym')
    response=HttpResponse()
    for i in x:
        response.write(f"{i['name']} <strong>{i['acronym']}</strong>")
        response.write('<br >')
        res=HttpResponse()
    #return HttpResponse(response)
    """Tried  returing the object directly but that doesnt work as the query set ob"""
    return render(request,'college_data.html',{'dataSet':x})

def list_of_students(request):
    response=Student.objects.values('id','name','email','college__acronym')
    return render(request,'student_data.html',{'dataSet':response})

def student_details(request,id):
    try:
        response=Student.objects.get(id=id)
        return render(request, 'student_details.html', {'dataSet': response})
    except Exception as e:
        return render(request, 'test.html',{'problem':e})


def list_of_students_collegewise(request,acronym):
    try:
        response=MockTest1.objects.filter(student__college__acronym=acronym).order_by('-total')
        return render(request,'college_student_list.html',{'dataSet':response})
    except:
        return render(request, 'test.html')

def testing_sessions(request):
    request.session['counter']=request.session.get('counter',0)+1
    #raise ValueError('just a test')
    return  HttpResponse(request.session['counter'])