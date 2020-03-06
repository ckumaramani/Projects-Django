from django.contrib import admin

from .models import Publications
from .models import Article

admin.site.register(Publications)
admin.site.register(Article)
