from django.contrib import admin

# Register your models here.
from .models import Topic,Entry # adding the Topic and Entry models from models.py 
# .models means in the same directory as admin.py
admin.site.register(Topic) # tells django to manage the model thru the admin site 
admin.site.register(Entry)
