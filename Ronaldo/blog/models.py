from django.db import models


# Create your models here.

class Home(models.Model):
    name = models.CharField(max_length=202)

    last_update = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=202)
    image = models.ImageField()
    text = models.TextField()
    name = models.CharField(max_length=202)
    birth = models.CharField(max_length=202)
    address = models.CharField(max_length=202)
    code = models.CharField(max_length=202)
    email = models.EmailField()
    phone = models.CharField(max_length=202)
    project = models.IntegerField()

    last_update = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Sponsor(models.Model):
    title = models.CharField(max_length=202)
    image = models.ImageField()

    def __str__(self):
        return self.title


class Service(models.Model):
    icon = models.CharField(max_length=202)
    title = models.CharField(max_length=202)
    text = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=202)
    text = models.CharField(max_length=202)
    image = models.ImageField()

    last_update = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=202)


    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=202)

    def __str__(self):
        return self.title

class Blog(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag")
    image = models.ImageField()
    title = models.CharField(max_length=202)
    text = models.CharField(max_length=303)
    content = models.TextField(null=True, blank=True)
    content_continued = models.TextField(null=True, blank=True)
    creative = models.TextField(null=True, blank=True)

    last_update = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]



class Contactme(models.Model):
    title = models.CharField(max_length=202)
    icon = models.CharField(max_length=202)
    text = models.CharField(max_length=303)

    def __str__(self):
        return self.title
