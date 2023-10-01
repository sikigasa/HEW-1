from django.contrib import admin
from . models import LoginUser
from . models import ImageUpload
# Register your models here.


admin.site.register(ImageUpload)
admin.site.register(LoginUser)
