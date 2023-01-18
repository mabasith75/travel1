from django.contrib import admin

from . models import lugar
from . models import team

# Register your models here.

admin.site.register(lugar)
admin.site.register(team)
