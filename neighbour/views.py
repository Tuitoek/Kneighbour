from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.contrib.auth.models import User

# Create your views here.
def landing(request):
    return render(request,'landing.html')



@login_required(login_url='/accounts/login/')
def editdp(request):
    return render(request,'profile/editdp.html')

@login_required(login_url='/accounts/login/')
def home(request):
    events = Events.objects.all()
    business=Business.objects.all()
    return render(request,'home2.html',{"events":events,"business":business})

@login_required(login_url='/accounts/login/')
def editdp(request):
    p_form = UserForm(request.POST,request.FILES)
    owner = request.user
    if request.method == 'POST':
        p_form =  UserForm(request.POST,request.FILES)
        if p_form.is_valid():
            add = p_form.save(commit=False)
            add.save()
            return render(request,'profile/profile.html')
        else:
            p_form =  UserForm(request.POST,request.FILES)

    return render(request,'profile/editdp.html',locals())

@login_required(login_url='/accounts/login/')
def profile(request):
    user=request.user
    profile = Profile.objects.all()
    return render(request,'profile/profile.html',{"profile":profile})

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def contacts(request):
    user = request.user
    contact = Contacts.objects.filter(user.neighbourhood)
    return render(request,"contact.html")

@login_required(login_url='/accounts/login/')
def search_hoods(request):
    if 'search' in request.GET and request.GET['search']:
        search_term=request.GET.get('search')
        searched_hoods=Neighbourhood.search_by_name(search_term)
        message=f'{search_term}'

        return render(request,'search.html',{"message":message,"searched_hoods":searched_hoods})

    else:
        message='You Havent searched for any term'

        return render(request, 'search.html',{"message":message})
    
