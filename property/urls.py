from django.urls import path
from .views import PropertyList, PropertyDetail
from . import views

app_name = 'property'


urlpatterns = [
    path('', PropertyList.as_view() , name='property_list'),
    # path('<slug:slug>', PropertyDetail.as_view() , name='property_detail'),

]