from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def landing(request):
    return render(request,'landing.html')

def profile(request):
    return render(request,'profile/profile.html')

def editdp(request):
    return render(request,'profile/editdp.html')

@login_required(login_url='/accounts/login/')
def home(request):
    return render(request,'home.html')
