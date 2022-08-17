from django.contrib import admin
from webapp.models import Contact
from webapp.models import Snacks
from webapp.models import Category, feedback

class AdminSnacks(admin.ModelAdmin):
    list_display = ['name', 'Price', 'category']

class AdminContact(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']

# class Admincustomer(admin.ModelAdmin):
#     list_display = ['', 'Price', 'category']

admin.site.register(Snacks, AdminSnacks)
admin.site.register(Category)
admin.site.register(feedback)
admin.site.register(Contact, AdminContact)



# Register your models here.

