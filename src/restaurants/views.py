from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"base.html",{'html_var':'testing','bool_item':'False'})

