from django.shortcuts import render
from .models import Logindetails

# Create your views here.
def elogin(request):
    return render(request,"login.html")


def savedetails(request):
    username=request.POST["uname"]
    password=request.POST["upass"]
    Logindetails.objects.get(username=username,password=password)
    return render(request,"welcome.html")










