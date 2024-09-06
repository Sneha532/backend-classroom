from django.contrib import admin

# Register your models here.
from .models import Users,classSubject,JoinClass,course,TD,TP,correction_TD_TP,Todo



class UsersAdmin(admin.ModelAdmin) :
    list_display  = ('nom','prenom','email','password','picture','role')

admin.site.register(Users,UsersAdmin)
admin.site.register(classSubject)
admin.site.register(JoinClass)
admin.site.register(course)
admin.site.register(TD)
admin.site.register(TP)
admin.site.register(correction_TD_TP)
admin.site.register(Todo)
