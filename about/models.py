from django.db import models

class About(models.Model):
    vision = models.TextField(max_length=1000)
    mission = models.TextField(max_length=1000)
    goals = models.TextField(max_length=1000)


    def __str__(self):
        return str(self.id)
    


class FAQ (models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=3000)

    def __str__(self):
        return self.title