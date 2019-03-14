from django.db import models

# Create your models here.
########################################################3
class city(models.Model):
    city_name = models.CharField(primary_key=True,max_length=128)
    city_price = models.IntegerField(default=1)
    in_the_usa = models.BooleanField(default=True)

    #class Meta:
        #abstract=True # because we have abstract file which create exlusive subtype

###################subtypes###########################3
class in_usa(city):
    State = models.CharField(max_length=128)


class out_usa(city):
   Country_name = models.CharField(max_length=128)
################################################################################





#Scooters tables
class s(models.Model): 
    s_sid = models.IntegerField(primary_key=True, default=0)
    s_availability = models.BooleanField(default=True)
    s_battery =models.IntegerField(default=0)
    s_pla = models.IntegerField(default=0) #position lattitude
    s_plo = models.IntegerField(default=0) #position longtitude
    s_city = models.ForeignKey(city, on_delete=models.CASCADE)
    
    
##############################################################################333
#Customers 
class c(models.Model): 
    c_LID = models.IntegerField(primary_key=True, default=0) #license ID
    c_name =models.CharField(max_length=128)
    #c_city = models.ForeignKey(in_usa, on_delete=models.CASCADE)
#we dont need city for users because they lose their felexibility to choose the city for themselves
    
######################################################################
class chargers(models.Model): 
    c_LID = models.IntegerField(primary_key=True, default=0) #license ID
    c_name =models.IntegerField(default=0)
###################################################################33
class cars(models.Model): 
    c_plnumber = models.IntegerField(primary_key=True, default=0) #license ID
    charger_id = models.ForeignKey(chargers,on_delete=models.CASCADE)

###########################################################################
class charger_scooter(models.Model): 
    charger_id = models.ForeignKey(chargers,on_delete=models.CASCADE) #license ID
    s_id = models.ForeignKey(s,on_delete=models.CASCADE)
    charged = models.IntegerField(default=0)
#############################################################################
class rented_scooters(models.Model): 
    c_id = models.ForeignKey(c,on_delete=models.CASCADE) #license ID
    s_id = models.ForeignKey(s,on_delete=models.CASCADE)
    duration = models.IntegerField(default=0)

    