from django.contrib import admin

from .models import Author,Category,Content
# Register your models here.


admin.site.register([Author,Category,Content])