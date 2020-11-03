from django.contrib import admin
from .models import student,studentmessage,Item
from embed_video.admin import AdminVideoMixin

# Register your models here.

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)

class studentAdmin(admin.ModelAdmin):
    list_display=["sname","degreegroup"]
admin.site.register(student,studentAdmin)
admin.site.register(studentmessage)
