from django.db import models
from django.contrib.auth.models import User
#  Create your models here.
#  @classmethod
#     def search_by_title(cls,search_term):
#         news = cls.objects.filter(title__icontains=search_term)
#         return news

class MoringaMerch(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)




class Project(models.Model):
    title = models.CharField(max_length = 60)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    url = models.CharField(max_length = 60)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='images/', default='/images/default.jpg')
    bio = models.TextField(blank=True)
    contacts = models.CharField(max_length = 30,blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Review(models.Model):
    design = models.IntegerField(default=0)
    usability = models.IntegerField(default=0)
    content = models.IntegerField(default=0)
    average = models.IntegerField(default=0)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.project.title