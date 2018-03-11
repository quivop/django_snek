from django.contrib import admin

from .models import Fanfic
from .models import Link

# Register your models here.
admin.site.register(Fanfic)
admin.site.register(Link)