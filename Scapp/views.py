from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def home(request):
    context = {
        'scooters' : s.objects.all()
    }
    return render(request, 'Scapp/home.html', context)
def about(request):
    return render(request, 'Scapp/about.html')
# Create your views here.

######################################Tables
def customers(request):
    context = {
        'customers' : c.objects.all()
    }
    return render(request, 'Scapp/customers.html', context)

def customers(request):
    context = {
        'customers' : c.objects.all()
    }
    return render(request, 'Scapp/customers.html', context)
def city_table(request):
    context = {
        'city' : city.objects.all()
    }
    return render(request, 'Scapp/city_table.html', context)
def scooters_table(request):
    context = {
        's' : s.objects.all()
    }
    return render(request, 'Scapp/scooters_table.html', context)
##################################################################Register Users
def register(request):
    my_form = customersForm()
    if request.method == "POST":
        my_form = customersForm(request.POST or None)
        
        if my_form.is_valid():
            print(my_form.cleaned_data)
            c.objects.create(**my_form.cleaned_data)
            return redirect('scooters_table')
            #form.save()
    context = {
        "form" : my_form
	}
    return render(request, "Scapp/register.html",context)
 
###############################################################with forms:

def city_input(request):
    my_form = cityForm()
    if request.method == "POST":
        my_form = cityForm(request.POST or None)
        
        if my_form.is_valid():
            print(my_form.cleaned_data)
            city.objects.create(**my_form.cleaned_data)
            return redirect('city_table')

            #form.save()
    context = {
        "form" : my_form
	}
    return render(request, "Scapp/city_input.html",context)
################################################################rent
def rent_input(request):
    my_form = rentForm()
    if request.method == "POST":
        my_form = rentForm(request.POST)
        
        if my_form.is_valid():
            print(my_form.cleaned_data)
            rented_scooters.objects.create(**my_form.cleaned_data)
            return redirect('city_table')

            #form.save()
    context = {
        "form" : my_form
	}
    return render(request, "Scapp/rent_input.html",context)

##################################################################scooters update

#def s_update1(request):
 #   if(request.method =='POST'):
  #      my_form = request.POST.get('form')
            
   # if my_form.is_valid():
    #    print(my_form.cleaned_data["battery"])
     #   s.objects.filter(s_sid = my_form.cleaned_data["sid"]).update(s_battery=my_form.cleaned_data["battery"],s_pla=my_form.cleaned_data["pla"],s_plo=my_form.cleaned_data["plo"],s_availability=my_form.cleaned_data["availability"])

      #  s.save()

 #   return render(redirect ="Scapp/scooters_table.html")


#########################################################scooter input

def scooters_input(request):
    my_form = scootersForm()
    if request.method == "POST":
        my_form = scootersForm(request.POST or None)
        
        if my_form.is_valid():
            print(my_form.cleaned_data)
            s.objects.create(**my_form.cleaned_data)
            return redirect('home')
            #form.save()
    context = {
        "form" : my_form
	}
    return render(request, "Scapp/scooters_input.html",context)


########################################################scooter Deletion:

def scooters_delete(request):
    my_form = delete_form()
    if request.method == "POST":
        my_form = delete_form(request.POST or None)
        
        if my_form.is_valid():
            print(my_form.cleaned_data["id"])
            s.objects.filter(s_sid = my_form.cleaned_data["id"]).delete()

            #form.save()
    context = {
        "form" : my_form
	}
    return render(request, "Scapp/scooters_delete.html",context)
##################################################################### counter
def cityfinder(request):
    my_form = countForm()
    if request.method == "POST":
        my_form = delete_form(request.POST or None)
        
        if my_form.is_valid():
            print(my_form.cleaned_data["City_Name"])
            #print( s.objects.filter(s_city.objects.filter(city_name) = my_form.cleaned_data["City_Name"])

           # s.objects.filter(s_city.objects.filter(city_name) = my_form.cleaned_data["City_Name"]#)
            #form.save()
    H = {
        "form" : my_form
	}
    return render(request, "Scapp/cityfinder.html",H)
