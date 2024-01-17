from django.urls import path
from .views import profile , profile_edit , signup , my_reservation ,my_listing, delete_property, add_feedback, logout, login
from . import views
from property.views import NewProperty

app_name = 'accounts'

urlpatterns = [
    # path('profile/', profile, name='profile'),
    # path('edit/', profile_edit, name='profile_edit') ,
    path('newproperty/', NewProperty.as_view(), name='property_new'),
    path('property/<int:property_id>/delete/', delete_property, name='delete_property'),
    path('profile/myreservation/', my_reservation, name='my_reservation') ,
    path('profile/mylisting/', my_listing, name='my_listing') ,
    path('profile/booking/<slug:slug>/review/', add_feedback, name='add_feedback') 
]
