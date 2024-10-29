from django.contrib import admin
from .models import Application, Qabul


admin.site.register([Application, Qabul])