from django.db import models
from django.urls import reverse



    


# class FAQ(models.Model):
#     title = models.CharField(max_length=150)
#     description = models.TextField(max_length=3000)

#     def __str__(self):
#         return self.title
    




class About(models.Model):
    what_we_do = models.TextField(max_length=1000)
    our_mission = models.TextField(max_length=1000)
    our_goal = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='about/')
    why_choose_us =  models.TextField(max_length=10000)

    class Meta:
        verbose_name = ("About")
        verbose_name_plural = ("About")

    def __str__(self):
        return str(self.id)

    # def get_absolute_url(self):
    #     return reverse("About_detail", kwargs={"pk": self.pk})



class FAQ(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    

    class Meta:
        verbose_name = ("FAQ")
        verbose_name_plural = ("FAQ")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("FAQ_detail", kwargs={"pk": self.pk})



