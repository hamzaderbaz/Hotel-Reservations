from audioop import reverse
from django.db import models


class Info(models.Model):

    name = models.CharField(max_length=30)
    email = models.EmailField(max_length= 254)
    phone_number = models.CharField(max_length= 20)
    address = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    logo = models.ImageField(upload_to="company/")
    fb_url = models.URLField(max_length=200 , blank=True, null=True)
    twitter_url = models.URLField(max_length=200 , blank=True, null=True)
    Instgram_url = models.URLField(max_length=200 , blank=True, null=True)
    

    class Meta:
        verbose_name = ("Info")
        verbose_name_plural = ("Infos")

    def __str__(self):
        return self.email

    # def get_absolute_url(self):
    #     return reverse("Info_detail", kwargs={"pk": self.pk})



