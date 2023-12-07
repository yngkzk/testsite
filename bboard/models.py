from django.db import models

# Create your models here.


class IceCream(models.Model):
    flavor = models.CharField(max_length=100)
    portion_size = models.CharField(max_length=50)
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    calories = models.PositiveIntegerField()

    def __str__(self):
        return self.flavor


class IceCreamKiosk(models.Model):
    location = models.CharField(max_length=200)
    available_flavors = models.ManyToManyField(IceCream)
    prices = models.TextField()
    working_hours = models.CharField(max_length=100)
    staff_info = models.TextField()
    special_offers = models.TextField()

    def __str__(self):
        return self.location


class Parent(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Child(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    school = models.CharField(max_length=100)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __str__(self):
        return self.name