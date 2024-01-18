from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

    
class Profile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    image = models.ImageField(upload_to='profile/', blank=True, null=True)
    phone_number = models.CharField(max_length=16, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.user)
    
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)




# # Model to store additional user profile information
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)  # One-to-one relationship with the User model
#     city = models.ForeignKey('City', related_name='user_city', on_delete=models.CASCADE, blank=True, null=True)  # City associated with the profile
    
#     def __str__(self):
#         return str(self.user)  # String representation of the profile (user's username)



# # Model to represent cities
# class City(models.Model):
#     name = models.CharField(max_length=30)  # Name of the city
    
#     def __str__(self):
#         return self.name  # String representation of the city (its name)
