from django.contrib import admin
from .models import Sastojci, Kategorije, Jela

# Register your models here.

admin.site.register(Sastojci)
admin.site.register(Kategorije)
admin.site.register(Jela)


