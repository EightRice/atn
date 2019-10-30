from django.contrib import admin
from .models import Agent
from .models import Mock
from .models import Product
from .models import Category

admin.site.register(Agent)
admin.site.register(Mock)
admin.site.register (Product)
admin.site.register(Category)

# Register your models here.
