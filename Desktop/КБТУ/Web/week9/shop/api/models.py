from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name
        }


class Product(models.Model):
    category = models.ForeignKey(on_delete=models.CASCADE, to=Category)
    name = models.CharField(max_length=100)
    price = models.FloatField(default=1000)
    description = models.TextField(max_length=500)
    count = models.IntegerField(default=0)

    def to_json(self):
        return {
            "id": self.id,
            "category": self.category.to_json(),
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "count": self.count
        }
