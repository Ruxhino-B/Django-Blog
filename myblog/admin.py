from django.contrib import admin
from .models import Post, Koment
from perdorues.models import Perdorues

# Register your models here.
admin.site.register(Post)
admin.site.register(Perdorues)
admin.site.register(Koment)