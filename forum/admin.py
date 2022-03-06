from django.contrib import admin
from .models import Section, Category, Topic, Post

models_to_register = [Section, Category, Topic, Post]
admin.site.register(models_to_register)
