from django.contrib import admin
from .models import Developer, Question, Choice

@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    pass

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass