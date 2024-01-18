from django.urls import path
from . import views
# from .views import contact
from .views import send_message

# from .views import contact

app_name = 'contact'



urlpatterns = [

    # path('', contact, name='contact'),
    path('', send_message, name='contact'),
]

