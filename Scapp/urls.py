from django.urls import path
from . import views
urlpatterns = [
#url(r'^$',views.my_view, name = 'h'),
#url(r'^admin/', admin.site.urls)
path('', views.home,name ='home'),
path('about/', views.about,name ='about'),
path('customers/', views.customers,name ='customers'),
##city
path('city_table/', views.city_table,name ='city_table'),
##
#path('chargers/', views.chargers,name ='chargers'),
##
#path('cars/', views.cars,name ='cars'),
##
#path('chargers_scooter/', views.chargers_scooter,name ='chargers_scooter'),
#path('rents/', views.rents,name ='rents'),
path('city_input/', views.city_input,name ='city_input'),
path('scooters_input/', views.scooters_input,name ='scooters_input'),
path('scooters_delete/', views.scooters_delete,name ='scooters_delete'),
#####customer signup:
path('register/', views.register,name ='register'),
path('scooters_table/', views.scooters_table,name ='scooters_table'),
path('rent_input/', views.rent_input,name ='rent_input'),
#path('s_update/', views.s_update,name ='s_update'),
#path('cityfinder/', views.cityfinder,name ='cityfinder'),
#path('s_update1/', views.s_update1,name ='s_update1'),
]
