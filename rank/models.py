from django.db import models

#  Create your models here.
#  @classmethod
#     def search_by_title(cls,search_term):
#         news = cls.objects.filter(title__icontains=search_term)
#         return news

class MoringaMerch(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)