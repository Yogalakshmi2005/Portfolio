from django.db import models

# Create your models here.

class About(models.Model):
    content = models.TextField()

class SkillGroup(models.Model):
    name = models.CharField(max_length=100)

class Skill(models.Model):
    group = models.ForeignKey(SkillGroup, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    icon_url = models.URLField()

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True)
    note = models.TextField(blank=True)

class Certification(models.Model):
    title = models.CharField(max_length=200)
    provider = models.CharField(max_length=200)
    status = models.CharField(max_length=100, blank=True)

class Contact(models.Model):
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    linkedin = models.URLField()
    github = models.URLField()

