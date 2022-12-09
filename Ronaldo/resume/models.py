from django.db import models


# Create your models here.


class Education(models.Model):
    title = models.CharField(max_length=202)
    start_finish = models.CharField(max_length=202)
    address = models.CharField(max_length=303)
    text = models.CharField(max_length=505)

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=202)
    start_finish = models.CharField(max_length=202)
    address = models.CharField(max_length=303)
    text = models.CharField(max_length=505)

    def __str__(self):
        return self.title


class Skill_one(models.Model):
    title = models.CharField(max_length=202, null=True, blank=True)
    percentage = models.IntegerField(null=True, blank=True)
    last_week = models.IntegerField(null=True, blank=True)
    last_month = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Skill_two(models.Model):
    name = models.CharField(max_length=202, null=True, blank=True)
    foiz = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Awards(models.Model):
    title = models.CharField(max_length=202)
    start_finish = models.CharField(max_length=202)
    address = models.CharField(max_length=303)
    text = models.CharField(max_length=505)

    def __str__(self):
        return self.title
