from django.contrib import admin
from research.models import Note, Paper, Course, Semester

# Register your models here.

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass


@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    pass