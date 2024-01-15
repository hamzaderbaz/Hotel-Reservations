from django.urls import path
from .views import profile , profile_edit , signup , my_reservation , add_feedback, logout


app_name = 'accounts'

urlpatterns = [
    path('signup/',signup , name='signup'),
    path('logout/',logout , name='logout'),
    path('profile/',profile,name='profile'),
    path('profile/edit/', profile_edit , name='profile_edit') ,
    path('profile/myreservation/', my_reservation , name='my_reservation') ,
    path('profile/booking/<slug:slug>/review/', add_feedback , name='add_feedback') 
]
