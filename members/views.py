from email import message
from urllib import request


from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

from members.models import members
from django.contrib import messages

# Create your views here.

def index(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def members_data(request):
    var = {"first_name":"Tossawat","last_name":"Kongkabin"}
    mData = members()
    mData.firstname = "Name"
    mData.lastname = "Surname"
    try:
        mData.save()
        messages.success(request,"Complete!")
    except:
        messages.success(request,"Try again!")
    finally:
        return render(request,"myfirst.html",var)

