from django.urls import path
from . import views
from . api_view import PropertyListApi, PropertyDetailApi


app_name = 'property'




urlpatterns = [

    path('', views.PropertyList.as_view() , name='property_list'),
    path('<slug:slug>/',views.PropertyDetail.as_view() , name='property_detail'),
    path('category/<str:category>/',views.property_by_category , name='property_by_category'),



    # API
    path('api_property_list/', PropertyListApi.as_view(), name='api_property_list'),
    path('api_property_detail/<int:pk>/', PropertyDetailApi.as_view(), name='api_property_detail')

]