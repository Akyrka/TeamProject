from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class Subject(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class SchoolClass(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject, blank=True)
    def __str__(self):
        return self.user.username

class DiaryEntry(models.Model):
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE,null=True, blank=True, related_name="diary_entries")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    homework = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.school_class} - {self.subject}"

class Schedule(models.Model):
    DAYS_OF_WEEK = [
        ('mon', 'Понеділок'),
        ('tue', 'Вівторок'),
        ('wed', 'Середа'),
        ('thu', 'Четвер'),
        ('fri', 'П’ятниця'),
        ('sat', 'Субота'),
    ]

    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    day_of_week = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    lesson_number = models.PositiveIntegerField() 
    start_time = models.TimeField()
    end_time = models.TimeField()

    def save(self, *args, **kwargs):
        if self.start_time:
            dt = datetime.combine(datetime.today(), self.start_time) + timedelta(minutes=45)
            self.end_time = dt.time()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.school_class} — {self.subject} ({self.day_of_week})"