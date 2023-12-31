from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    author = models.ForeignKey(User,related_name='post_author' , on_delete=models.CASCADE , verbose_name=_('author'))
    name = models.CharField(max_length=100 , verbose_name=_('name'))
    tags = TaggableManager()
    image = models.ImageField(_('image') ,upload_to='blog/')
    description = models.TextField(max_length=10000 , verbose_name=_('description'))
    created_at = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('Category', related_name='post_category', on_delete=models.CASCADE , verbose_name=_('category'))
    slug = models.SlugField(blank=True, null=True)
    

    def save(self, *args, **kwargs):
        if self.name:
            self.slug = slugify(self.name)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})
    



class Category(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(blank=True, null=True)
    # slug = models.SlugField(unique=True)


    def save(self, *args, **kwargs):
        if self.name:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name



