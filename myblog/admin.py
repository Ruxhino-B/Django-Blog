from django.contrib import admin
from .models import Post, Koment, Kategori
from perdorues.models import Perdorues

# Register your models here.
admin.site.register(Post)
admin.site.register(Perdorues)
admin.site.register(Koment)
admin.site.register(Kategori)