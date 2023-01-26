from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    subject = models.TextField(blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name

class Information(models.Model):
    address1 = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.address1

class Upcoming(models.Model):
    image1 = models.ImageField(upload_to='media')
    image2 = models.ImageField(upload_to='media')
    club1 = models.CharField(max_length=100)
    club2 = models.CharField(max_length=100)
    league = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    arena = models.CharField(max_length=100)

    def __str__(self):
        return self.club1

class Blog(models.Model):
    image = models.ImageField(upload_to='media')
    date = models.CharField(max_length=100)
    subject = models.TextField(max_length=300)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.date

class Table(models.Model):
    position = models.CharField(max_length=50)
    club = models.CharField(max_length=100)
    point = models.CharField(max_length=50)
    win = models.CharField(max_length=50)
    lose = models.CharField(max_length=50)
    draw = models.CharField(max_length=50)

    def __str__(self):
        return self.position

class Finale(models.Model):
    image1 = models.ImageField(upload_to='media')
    image2 = models.ImageField(upload_to='media')
    club1 = models.CharField(max_length=100)
    club2 = models.CharField(max_length=100)
    league = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    arena = models.CharField(max_length=100)

    def __str__(self):
        return self.club1

class Wcup(models.Model):
    image1 = models.ImageField(upload_to='media')
    image2 = models.ImageField(upload_to='media')
    country1 = models.CharField(max_length=100)
    country2 = models.CharField(max_length=100)
    score = models.CharField(max_length=100)

    def __str__(self):
        return self.country1

class Stat(models.Model):
    image = models.ImageField(upload_to='media')
    position = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name






