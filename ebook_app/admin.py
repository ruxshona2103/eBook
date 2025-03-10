from django.contrib import admin
from ebook_app.models import *

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Order)

