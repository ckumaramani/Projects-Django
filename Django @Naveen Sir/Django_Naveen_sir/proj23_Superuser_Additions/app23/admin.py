from django.contrib import admin

from .models import staff
from .models import user

admin.site.register(staff)
admin.site.register(user)

