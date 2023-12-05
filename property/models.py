from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Property(models.Model):
    owner = models.ForeignKey(User, related_name='property_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=12000)
    price = models.IntegerField()
    place = models.ForeignKey('Place', related_name='property_place', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='propery/')
    category = models.ForeignKey('Category', related_name='property_category', on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Properties'

    def save(self, *args, **kwargs):
        if self.title:
            self.slug = slugify(self.title)
        super(Property, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('property:property_detail' , kwargs={'slug':self.slug})