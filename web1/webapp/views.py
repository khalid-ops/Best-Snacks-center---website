from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from webapp.models import Contact, Snacks, Category, feedback
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from webapp.serializer import SnacksSerializer, ContactSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import filters
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
import requests
from django.core.mail import send_mail

# Create your views here.
@api_view(['GET'])
def rapi_snack(request):
    if request.method == "GET":
        results = Snacks.objects.all()
        serialize = SnacksSerializer(results, many=True)
        return Response(serialize.data)


@api_view(['GET'])
def north_filter(request):
    if request.method == "GET":
        results = Snacks.objects.all().filter(category=1)
        serialize = SnacksSerializer(results, many=True)
    return Response(serialize.data)

@api_view(['GET'])
def south_filter(request):
    if request.method == "GET":
        results = Snacks.objects.all().filter(category=2)
        serialize = SnacksSerializer(results, many=True)
    return Response(serialize.data)

@api_view(['GET'])
def inter_filter(request):
    if request.method == "GET":
        results = Snacks.objects.all().filter(category=3)
        serialize = SnacksSerializer(results, many=True)
    return Response(serialize.data)

@api_view(['GET'])
def contactapi(request):
    if request.method == "GET":
        results = Contact.objects.all()
        serialize = ContactSerializer(results, many=True)
    return Response(serialize.data)     

class search_filter(ListAPIView):
    queryset = Snacks.objects.all()
    serializer_class = SnacksSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']


def index(request):
    display_products = requests.get('http://127.0.0.1:8000/snacks')
    disp_data = display_products.json()

    return render(request, "index.html", {'Snacks':disp_data})

def about(request):
    return render(request, "about.html")

    # return HttpResponse('This is about homepage!!')

def n_display(request):
    display_products1 = requests.get('http://127.0.0.1:8000/north')
    disp_data1 = display_products1.json()
    return render(request, "nfilters.html", {'Snacks': disp_data1})

def s_display(request): 
    display_products2 = requests.get('http://127.0.0.1:8000/south')
    disp_data2 = display_products2.json()
    return render(request, "sfilters.html", {'Snacks': disp_data2})

def i_display(request):
    display_products3 = requests.get('http://127.0.0.1:8000/inter')
    disp_data3 = display_products3.json()
    return render(request, "ifilters.html", {'Snacks': disp_data3})

def con_display(request):
    display_contacts = requests.get('http://127.0.0.1:8000/contactapi')
    disp_data = display_contacts.json()
    return render(request, "contactinfo.html", {'Contact': disp_data})

def search_display(request):
    if request.method =="POST":
        searched_data = request.POST.get('searched')
        link = 'http://127.0.0.1:8000/search?search='
        s_link = link + searched_data
        display_products3 = requests.get(s_link)
        disp_data3 = display_products3.json()
        return render(request, "search.html", {'Snacks': disp_data3})
 

    # return HttpResponse('This is services page!!')
    
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact_obj = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact_obj.save()
        messages.success(request, 'Thankyou for contacting us! Form Submitted successfully.')

    return render(request, "contact.html")

    # return HttpResponse('This is contact page!')
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.success(request, ('Error! Try again'))
            return redirect('login.html')
    
    return render(request, "login.html")



def logout_user(request):
    logout(request)
    messages.success(request, ('you are logged out'))
    return redirect('/')



def feedbacksend_mail(request):
    message= 'Thanks for feedback'
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        feedb = request.POST.get('feedb')
        feedback_obj = feedback(name=name, email=email, feedb=feedb)
        feedback_obj.save()

        sub = 'confirmation'
        send_mail(
        sub,
        message,
        'mohammedkhalid1998@gmail.com',
        [email]
        )
    return render(request, 'feedback.html',)

def signup(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, "Welcome to the snack world")
                return redirect("/")
        else:
            form = UserCreationForm()
        return render(request, 'signup.html', {'form':form})
    else:
        return HttpResponse("Sorry! only Admin can add the users")









