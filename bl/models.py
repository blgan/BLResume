from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class About(models.Model):

    objects = None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img')
    address = models.TextField()
    phone_number = PhoneNumberField()
    email = models.EmailField()
    description = models.TextField()


class Experience(models.Model):

    objects = None
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    description = models.TextField()


class Education(models.Model):

    objects = None
    school_name = models.CharField(max_length=100)
    certificate = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    cgpa = models.FloatField()


class Skill(models.Model):

    objects = None
    skill_title = models.CharField(max_length=100)
    skill_knowledge_title = models.CharField(max_length=100)
    skill_knowledge_1 = models.CharField(max_length=100)
    skill_knowledge_2 = models.CharField(max_length=100)
    skill_knowledge_3 = models.CharField(max_length=100)
    skill_knowledge_4 = models.CharField(max_length=100)


class Language(models.Model):

    objects = None
    language = models.CharField(max_length=100)


class Award(models.Model):

    objects = None
    award = models.CharField(max_length=100)

