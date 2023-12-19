from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Category)
admin.site.register(models.Order)
admin.site.register(models.Product)
admin.site.register(models.Customer)

admin.site.site_header = "Mr.Coffee Admin"
admin.site.site_title = "Mr.Coffee Panel"
admin.site.index_title = "Mr.Coffee Coffee store Admin"
