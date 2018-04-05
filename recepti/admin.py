from django.contrib import admin
from .models import Sastojci, Kategorije, Jela, SastojciUJelu, User

# Register your models here.

admin.site.register(Sastojci)
admin.site.register(Kategorije)
admin.site.register(Jela)
admin.site.register(SastojciUJelu)
admin.site.register(User)



