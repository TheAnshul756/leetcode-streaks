from django.contrib import admin

# Register your models here.

from .models import Question, User, SolvedData

admin.site.register([Question, User, SolvedData])