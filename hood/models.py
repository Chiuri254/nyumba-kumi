from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.

# class Business(models.Model):
#     logo = models.ImageField(upload_to='businesslogo/')
#     description = HTMLField()
#     neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
#     owner = models.ForeignKey(User,on_delete=models.CASCADE)
#     name =models.CharField(max_length=100)
#     email = models.EmailField()
#     address =models.CharField(max_length=100)
#     contact = models.IntegerField()

#     def __str__(self):
#         return self.name
class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    @classmethod
    def delete_category(cls,name):
        cls.objects.filter(name = name).delete()

class Location(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    @classmethod
    def delete_location(cls,name):
        cls.objects.filter(name = name).delete()

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 30)
    image_description = models.TextField()
    image_category = models.ForeignKey(Category,on_delete = models.CASCADE)
    image_location = models.ForeignKey(Location,on_delete = models.CASCADE)

    def save_image(self):
        self.save()

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(image_category__name__contains = search_term)
        return images

class neighbourhood(models.Model):
    neighbourhood= models.CharField(max_length=100)

    def __str__(self):
        return self.neighbourhood

    def save_neighbourhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood(cls,neighbourhood):
        cls.objects.filter(neighbourhood=neighbourhood).delete()

class healthservices(models.Model):
    healthservices = models.CharField(max_length=100)

    def __str__(self):
        return self.healthservices

    def save_healthservices(self):
        self.save()

    @classmethod
    def delete_healthservices(cls,healthservices):
        cls.objects.filter(healthservices=healthservices).delete()



class Health(models.Model):
    logo = models.ImageField(upload_to='healthlogo/')
    neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address =models.CharField(max_length=100)
    healthservices = models.ManyToManyField(healthservices)

    def __str__(self):
        return self.name

class Authorities(models.Model):
    neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address =models.CharField(max_length=100)

    def __str__(self):
        return self.name
