from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
 
 

def index(request):
    return render(request,"index.html")
