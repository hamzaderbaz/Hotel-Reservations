from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin


from .models import Post, Category

class SomeModelAdmin(SummernoteModelAdmin):  
    summernote_fields = '__all__'


admin.site.register(Post, SomeModelAdmin)
admin.site.register(Category)