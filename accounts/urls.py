from django.urls import path
from .views import profile , profile_edit , signup , my_reservation ,my_listing, add_feedback, logout
from . import views
from property.views import NewProperty

app_name = 'accounts'

urlpatterns = [
    path('signup/',signup , name='signup'),
    path('logout/',logout , name='logout'),
    path('profile/',profile,name='profile'),
    path('editprofile/', profile_edit , name='profile_edit') ,
    path('newproperty/', NewProperty.as_view() , name='property_new'),
    path('profile/myreservation/', my_reservation , name='my_reservation') ,
    path('profile/mylisting/', my_listing, name='my_listing') ,
    path('profile/booking/<slug:slug>/review/', add_feedback , name='add_feedback') 
]
