from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def index(request):
    now=datetime.datetime.now()
    return render(request,"Countdown/index.html",{
        "birthday": now.month == 5 and now.day == 22
    })