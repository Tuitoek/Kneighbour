from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def landing(request):
    return render(request,'landing.html')

def profile(request):
    return render(request,'profile/profile.html')

def editdp(request):
    return render(request,'profile/editdp.html')  
