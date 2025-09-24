from django.db import models

# Create your models here.
class CartModel(models.Model):
    # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField()
    def __str__(self):
        return self.title
