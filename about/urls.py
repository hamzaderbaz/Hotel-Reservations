from django.urls import path
from .views import AboutView
from . import views
# from . import api_view


app_name = 'about'


urlpatterns = [

    path('', AboutView.as_view(), name='about'),
    # path( 'dashboard/',views.dashboard , name='dashboard' ),

    # path( 'about/api',api_view.about_api , name='about_api' ),
    # path( 'about/api/faq',api_view.faq_api , name='faq_api' ),
    # path( 'contact/api',api_view.contact_api , name='contact_api' ),

]