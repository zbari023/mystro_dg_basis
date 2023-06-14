from django.contrib import admin

# Register your models here.
from .models import mypost , Autor
admin.site.register(mypost)
admin.site.register(Autor)