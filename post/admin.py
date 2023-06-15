from django.contrib import admin

# Register your models here.
from .models import mypost , Autor
class mypostAdmin(admin.ModelAdmin):
    list_display = ['title' , 'publishedDate','autor']
    list_filter =  ['autor']
    search_fields = ['autor']
admin.site.register(mypost, mypostAdmin)
admin.site.register(Autor)