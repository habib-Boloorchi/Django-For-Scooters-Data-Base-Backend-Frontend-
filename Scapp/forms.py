from django import forms
from .models import *
class cityForm(forms.Form):
    city_name = forms.CharField(max_length=128)
    city_price = forms.IntegerField()
    in_the_usa = forms.BooleanField(required=False)
    class Meta:
        # Provide an association between the ModelForm and a model
        model = city
#class cityf(forms.ModelForm):
 #   class Meta:
  #      mycity = in_usa
#	fields = [
#	    'city_name',
#	    'price',
 #	    'State'= 
#	]
class scootersForm(forms.Form):
    s_sid = forms.IntegerField(label='Scooter id')    
    s_battery = forms.IntegerField(label='Battery')
    s_pla = forms.IntegerField(label='Lattitude')    
    s_plo = forms.IntegerField(label='Longtitude')
    s_availability = forms.BooleanField(required=False,label='Is it available?')
    
    s_city = forms.ModelChoiceField(queryset=city.objects.all(),label='City')
    class Meta:
        # Provide an association between the ModelForm and a model
        model = s
##################################################delete
class delete_form(forms.Form):
    id = forms.IntegerField()    
   ###################################################customersform
class customersForm(forms.Form):
    c_LID = forms.IntegerField(label='customer license id')    
    c_name= forms.CharField(max_length=128,label='customer name')

    class Meta:
        # Provide an association between the ModelForm and a model
        model = c

##############################################rentform
class rentForm(forms.Form):
    c_id = forms.ModelChoiceField(queryset=c.objects.all(),label='customer license id')    
    s_id= forms.ModelChoiceField(queryset=s.objects.all(),label='scooter id')
    duration=forms.IntegerField()

    class Meta:
        # Provide an association between the ModelForm and a model
        model = rented_scooters
######################################################scooter update
#class scootersForm(forms.Form):
 
#   s_sid = forms.IntegerField()    
 
#   s_battery = forms.IntegerField()
 #   s_pla = forms.IntegerField()    
  #  s_plo = forms.IntegerField()
   # s_availability = forms.BooleanField(required=True)
    
    #s_city = forms.ModelChoiceField(queryset=city.objects.all())
    #class Meta:
        # Provide an association between the ModelForm and a model
     #   model = s
###########################################################################scooter update
class updateForm(forms.Form):
    sid = forms.IntegerField()    
    battery = forms.IntegerField(required=False)
    pla = forms.IntegerField(required=False)    
    plo = forms.IntegerField(required=False)
    availability = forms.BooleanField(required=False)
    
class countForm(forms.Form):
   city_name = forms.CharField(max_length=128)  
   class Meta:
        # Provide an association between the ModelForm and a model
        model = city
	 

