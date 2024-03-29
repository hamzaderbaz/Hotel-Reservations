from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, FAQ



class SomeModelAdmin(SummernoteModelAdmin):  
    summernote_fields = '__all__'



admin.site.register(About, SomeModelAdmin)
admin.site.register(FAQ, SomeModelAdmin)