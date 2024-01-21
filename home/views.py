from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
# from .models import FAQ , About , Info
from property import models as property_models
from property.models import Category, Property
from blog import models as blog_models
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.core.mail import send_mail
from django.conf import settings

# from .tasks import send_mail_task




def home(request):

    property_category = property_models.Category.objects.all()
    places = property_models.Place.objects.all().annotate(property_count=Count('property_place'))[:5]

    
    restaurants_list = property_models.Property.objects.filter(category__name='Restaurants')[:5]
    hotels_list = property_models.Property.objects.filter(category__name='Hotels')[:5]
    places_list = property_models.Property.objects.filter(category__name='Places')[:5]
    recent_posts = blog_models.Post.objects.all()[:4]

    # about = About.objects.last()

    users_count = User.objects.all().count()
    restaurants_count = property_models.Property.objects.filter(category__name='Restaurants').count()
    hotels_count = property_models.Property.objects.filter(category__name='Hotels').count()
    places_count = property_models.Property.objects.filter(category__name='Places').count()

    # places = property_models.Place.objects.all()[:2]


    return render(request,'home/home.html', {
        
        'property_category': property_category , 
        'recent_posts' : recent_posts , 
        'restaurants_list': restaurants_list , 
        'hotels_list' : hotels_list , 
        'places_list' : places_list ,

        'users_count' : users_count , 
        'restaurants_count': restaurants_count , 
        'hotels_count' : hotels_count  , 
        'places_count' : places_count , 
        'places':places,

    })



def home_search(request):
    name = request.GET.get('q', '')
    location = request.GET['location']

    property_list = Property.objects.filter(
            Q(place__name__icontains=location) &
            Q(name__icontains=name) 
            # Q(description__icontains=name) 

    )

    return render(request,'home/home_search.html', {'property_list': property_list})


def category_filter(request, category):
    # category = get_object_or_404(Category, name=category)
    category = Category.objects.get(name=category)
    property_list = Property.objects.filter(category=category)
    return render(request,'home/home_search.html', {'property_list': property_list})












def dashboard(request):
    
    users_count = User.objects.all().count()
    appartments_count = property_models.Property.objects.filter(category__name='Apparment').count()
    villa_count = property_models.Property.objects.filter(category__name='Vella').count()
    suits_count = property_models.Property.objects.filter(category__name='suite').count()
    posts = blog_models.Post.objects.all().count()
    booking = property_models.PropertyBook.objects.all().count()

    return render(request,'home/dashboard.html',{
        'users_count' : users_count , 
        'appartments_count': appartments_count , 
        'villa_count' : villa_count  , 
        'suits_count' : suits_count ,  
        'posts_count' : posts , 
        'booking_count' : booking
    })