from django import views
from django.urls import path , include
from django.contrib import admin 
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from accounts import views
from property.views import NewProperty

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    
    openapi.Info(
        title='Booking.com',
        default_version='v1',
        description="Booking.com API",
        terms_of_service="https://www.booking.com/terms/",
        contact=openapi.Contact(email="contact@booking.com"),
        license=openapi.License(name="Booking.com License"),
    ),
    public=True,
)





urlpatterns = [


    # apps
    
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),  # This is the URL for the home page
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('hotels/', include('property.urls', namespace='property')),
    path('blog/' , include('blog.urls' , namespace='blog')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('about/', include('about.urls', namespace='about')),
    path('summernote/', include('django_summernote.urls')),
    


    # URL of registrations
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),


    # URL of accounts app
    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.profile_edit, name='profile_edit'),
    path('addproperty/', NewProperty.as_view(), name='property_new'),
    path('profile/myreservation/', views.my_reservation, name='my_reservation'),
    path('profile/mylisting/', views.my_listing, name='my_listing'),
    path('profile/mylisting/<int:property_id>/', views.delete_property, name='delete_property'),
    path('profile/myreservation/<slug:slug>/', views.add_feedback, name='add_feedback'),




    # path('rate/<int:post_id>/<int:rating>/', views.rate),
    # path('ratings/', include('star_ratings.urls', namespace='ratings')),



    # API
    # path('api/', include('Vending_Machine.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 




]




if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  






    