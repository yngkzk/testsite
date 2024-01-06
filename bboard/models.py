from django.core.exceptions import ValidationError
from django.db import models


def validate_positive(val):
    if val < 0:
        raise ValidationError(
            'Число %(value)s отрицательное',
            code='odd',
            params={'value': val}
        )
    return True


class IceCream(models.Model):
    flavor = models.CharField(max_length=100)
    portion_size = models.CharField(max_length=50)
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[validate_positive])
    calories = models.PositiveIntegerField()

    def __str__(self):
        return self.flavor

    def give_id(self):
        return f"{self.flavor} - {self.give_id()}"


class IceCreamKiosk(models.Model):
    location = models.CharField(max_length=200)
    available_flavors = models.ManyToManyField(IceCream)
    prices = models.TextField()
    working_hours = models.CharField(max_length=100)
    staff_info = models.TextField()
    special_offers = models.TextField()

    def __str__(self):
        return self.location

    def give_id(self):
        return f"{self.location} - {self.give_id()}"


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


class Comment(models.Model):
    text = models.CharField(max_length=100, verbose_name='Текст')
    sender = models.CharField(max_length=100, verbose_name='Отправитель')

    def __str__(self):
        return f"{self.text[:20]} sender - {self.sender}"
