from django.urls import path
from . import views
# from . import api_view


app_name = 'home'


urlpatterns = [

    path('', views.home , name='home'),    
    path('search/', views.home_search , name='home_search'),    
    path('category/<slug:category>/', views.category_filter, name='category_filter'),   
    # path( 'dashboard/',views.dashboard , name='dashboard' ),

]
