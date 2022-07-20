from django.contrib import admin
from .models import Membership, Routine,Ovauser,Product,Ovauser_debt

admin.site.register(Routine)
admin.site.register(Membership)
admin.site.register(Ovauser)
admin.site.register(Product)
admin.site.register(Ovauser_debt)

# Register your models here.
    