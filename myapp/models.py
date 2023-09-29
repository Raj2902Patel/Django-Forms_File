from django.db import models

# Create your models here.

class data(models.Model):
    productname = models.CharField(max_length=50)
    productbrand = models.CharField(max_length=50)

    def __str__(self):
        return self.productbrand
