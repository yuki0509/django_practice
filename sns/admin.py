from django.contrib import admin
from . models import Message, Group, Friend, Good

# Register your models here.
admin.site.register(Message)
admin.site.register(Friend)
admin.site.register(Group)
admin.site.register(Good)
