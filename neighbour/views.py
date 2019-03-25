from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.contrib.auth.models import User

# Create your views here.
def landing(request):
    return render(request,'landing.html')

def profile(request):
    return render(request,'profile/profile.html')

def editdp(request):
    return render(request,'profile/editdp.html')

@login_required(login_url='/accounts/login/')
def home(request):
    events = Events.objects.all()
    business=Business.objects.all()
    return render(request,'home2.html',{"events":events,"business":business})

def editdp(request):
    p_form = UserForm(request.POST,request.FILES)
    owner = request.user
    if request.method == 'POST':
        p_form =  UserForm(request.POST,request.FILES)
        if p_form.is_valid():
            add = p_form.save(commit=False)
            add.save()
            return render(request,'profile.html')
    else:
        p_form =  UserForm(request.POST,request.FILES)

    return render(request,'profile/editdp.html',locals())

def profile(request):
    user=request.user
    profile = Owner.objects.get(user = user)
    return render(request,'profile/profile.html',locals())

def business(request):
    form = BusinessForm(request.POST,request.FILES)
    if request.method == 'POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            add = form.save(commit=False)
            add.save()
            return render(request,'home2.html')
    else:
        form =  BusinessForm(request.POST,request.FILES)
    return render(request,'business.html',locals())

def events(request):
    form = EventsForm(request.POST)
    if request.method == 'POST':
        form = EventsForm()
        if form.is_valid():
            form.save()
            return render(request,'home2.html')
    else:
        form =  EventsForm(request.POST)


    return render(request,'events.html',locals())

def contacts(request):
    user = request.user
    contact = Contacts.objects.filter(user.neighbourhood)
