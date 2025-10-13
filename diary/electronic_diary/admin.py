from django.contrib import admin
from .models import Teacher, Subject, SchoolClass, DiaryEntry, Schedule

admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(SchoolClass)
admin.site.register(DiaryEntry)
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('school_class', 'day_of_week', 'lesson_number', 'subject', 'teacher')
    list_filter = ('school_class', 'day_of_week')
    ordering = ('school_class', 'day_of_week', 'lesson_number')