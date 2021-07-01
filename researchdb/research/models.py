from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Note(models.Model):
    txt = models.CharField(max_length=4096, default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")

class Paper(models.Model):
    title = models.CharField(max_length=128, default="The Design and Implementation of a Log-Structured File System", validators=[RegexValidator(regex=r"^([0-9a-zA-Z]+\s{0,1})*$", message="Paper title can only contain alphanumeric and space characters.", code="paper-title")])
    notes = models.ManyToManyField(Note, blank=True)

class Course(models.Model):
    name = models.CharField(max_length=128, blank=True, default="Distributed and Cloud-Based Storage Systems", validators=[RegexValidator(regex=r"^([0-9a-zA-Z]+\s{0,1})*$", message="Course name can only contain alphanumeric and space characters.", code="course-name")])
    papers = models.ManyToManyField(Paper, blank=True)

class Semester(models.Model):
    name = models.CharField(max_length=128, default="Fall 2021", blank=True, validators=[RegexValidator(regex=r"^([0-9a-zA-Z]+\s{0,1})*$", message="Semester can only contain alphanumeric and space characters.", code="semester-name")])
    courses = models.ManyToManyField(Course, blank=True)

