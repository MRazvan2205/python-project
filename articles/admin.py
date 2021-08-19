from django.contrib import admin
from articles.models import Article, Comments

# Register your models here.

admin.site.register(Article)
admin.site.register(Comments)
