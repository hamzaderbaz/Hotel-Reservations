from django.urls import path
from . import views
from .api_view import PropertyListApi, PropertyDetailApi
# from django.db import router
# from rest_framework.routers import DefaultRouter


app_name = 'property'


# router = DefaultRouter()


urlpatterns = [

    path('',views.PropertyList.as_view() , name='property_list' ),
    path('<slug:slug>/',views.PropertyDetail.as_view() , name='property_detail'),
    path('category/<str:category>/',views.property_by_category , name='property_by_category'),



    # API
    # path('', include(router.urls)),
    path('property_api/', PropertyListApi.as_view(), name='property_api'),
    path('api/list/<int:pk>/', PropertyDetailApi.as_view(), name='property_api_detail'),

]