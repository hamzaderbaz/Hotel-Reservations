from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
from django.urls import reverse
# from django.utils import timezone



class Property(models.Model):
    # owner = models.ForeignKey(User, related_name='property_owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='propery/')
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=12000)
    place = models.ForeignKey('Place', related_name='property_place', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', related_name='property_category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    # created_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(blank=True, null=True)
    

    def save(self, *args, **kwargs):
        if self.name:
            self.slug = slugify(self.name)
        super(Property, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("property:property_detail", kwargs={"slug": self.slug})
    




class PropertyImages(models.Model):
    property = models.ForeignKey(Property, related_name='property_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return str(self.property)





class Place(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField( upload_to='places/')


    def __str__(self):
        return self.name
    


class Category(models.Model):
    name = models.CharField(max_length=25)

        
    def __str__(self):
        return self.name





class PropertyReview(models.Model):

    author = models.ForeignKey(User, related_name='review_owner', on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name='property_review', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0 ,  validators=[MaxValueValidator(5)])
    feedback = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.property)




PEOPLE_TYPE = (
    (1,1),
    (2,2),
    (3,3),
    (4,4)
)


class PropertyBook(models.Model):

    user = models.ForeignKey(User, related_name='user_book', on_delete=models.CASCADE) 
    property = models.ForeignKey(Property, related_name='property_book', on_delete=models.CASCADE)
    date_from = models.DateField(auto_now=True)
    date_to =  models.DateField(auto_now=True)
    guest = models.IntegerField(default=1 , choices=PEOPLE_TYPE)
    children = models.IntegerField(default=0 , choices=PEOPLE_TYPE)
    # slug = models.SlugField(blank=True, null=True)




    def __str__(self):
        return str(self.property)
    


