from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Lead)
admin.site.register(Organizer)
admin.site.register(Category)
