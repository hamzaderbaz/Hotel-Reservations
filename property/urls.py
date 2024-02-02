from django.urls import path
from . import views
from . api_view import PropertyListApi, PropertyDetailApi
# from django.db import router
# from rest_framework.routers import DefaultRouter


app_name = 'property'


# router = DefaultRouter()


urlpatterns = [

    path('', views.PropertyList.as_view() , name='property_list' ),
    path('<slug:slug>/',views.PropertyDetail.as_view() , name='property_detail'),
    path('category/<str:category>/',views.property_by_category , name='property_by_category'),



    # API
    # path('', include(router.urls)),
    path('api/property_api_list', PropertyListApi.as_view(), name='property_api_list'),
    path('api/property_api_detail/<int:pk>', PropertyDetailApi.as_view(), name='property_api_detail')

]