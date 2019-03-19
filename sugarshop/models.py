from django.core.validators import MaxLengthValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=2000,validators=[MaxLengthValidator(2000)])

    def __str__(self):
        return self.name


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    pic = models.ImageField(upload_to="productpics")
    description = models.CharField(max_length=2000,validators=[MaxLengthValidator(2000)])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def getConstituents(self):
        ids = []
        # Get all composition associated with this product
        for comp in Composition.objects.filter(product_id__exact=self.id):
            ids.append(comp.constituent.id)
        return Constituent.objects.filter(id__in=ids)




class Constituent(models.Model):
    MEDICAL = (
        ('ht', 'Heart attack'),
        ('fld', 'Fatty liver and diabetes'),
        ('d', 'Diarrhea'),
        ('c', 'Constipation'),
    )
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=2000,validators=[MaxLengthValidator(2000)])
    likely_consequence = models.CharField(choices=MEDICAL, max_length=10)

    def __str__(self):
        return self.name


class Composition(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    constituent = models.ForeignKey(Constituent, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name + " -> " + self.constituent.name
