from django.db import models



class Settings(models.Model):

    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='settings/')
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    fb_link = models.URLField(max_length=200)
    twit_link = models.URLField(max_length=200)
    insta_link = models.URLField(max_length=200)


    def __str__(self):
        return self.name