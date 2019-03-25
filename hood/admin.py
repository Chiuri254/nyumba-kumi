from django.contrib import admin
from .models import Category,Location,Image,healthservices,Authorities,neighbourhood
# Register your models here.
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Image)
# admin.site.register(Business)
admin.site.register(healthservices)
admin.site.register(Authorities)
admin.site.register(neighbourhood)