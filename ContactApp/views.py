from django.shortcuts import render
from django.http import HttpResponse
from .forms import contactform

def getContactPage(request):
    contact = contactform()
    return render(request, 'formtag.html', {'form': contact})

def Validate(request):
    return HttpResponse("Validate")