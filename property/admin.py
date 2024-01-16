from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# from tof.admin import TofAdmin, TranslationTabularInline
from .models import Property, PropertyImages, Place, Category, PropertyReview, PropertyBook


class SomeModelAdmin(SummernoteModelAdmin):  
    summernote_fields = '__all__'
    list_display= ['name' , 'check_avablity' , 'get_avg_rating']

    
admin.site.register(Property, SomeModelAdmin)

class RoomBookAdmin(admin.ModelAdmin):
    list_display = ['property','in_progress']

admin.site.register(PropertyBook, RoomBookAdmin)

admin.site.register(Category)


admin.site.register(PropertyImages)
admin.site.register(Place)
admin.site.register(PropertyReview)










# class CategoryAdmin(TofAdmin):
#     list_display = ('id', 'name')
#     inlines = (TranslationTabularInline, )

# admin.site.register(Category , CategoryAdmin)
