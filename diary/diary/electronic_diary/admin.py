from django.contrib import admin
from .models import Teacher, Subject, SchoolClass, DiaryEntry

admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(SchoolClass)
admin.site.register(DiaryEntry)
