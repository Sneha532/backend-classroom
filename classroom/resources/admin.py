from django.contrib import admin

# Register your models here.
from .models import Users



class UsersAdmin(admin.ModelAdmin) :
    list_display  = ('nom','prenom','email','password','picture','role')

admin.site.register(Users,UsersAdmin)