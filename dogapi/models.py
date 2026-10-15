from django.db import models

# Create your models here.
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Breed(models.Model):
    SIZE_CHOICES = [
        ("Tiny", "Tiny"),
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large"),
    ]

    name = models.CharField(max_length=100)
    size = models.CharField(max_length=6, choices=SIZE_CHOICES)
    friendliness = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    trainability = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    sheddingamount = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    exerciseneeds = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=50)
    color = models.CharField(max_length=100)
    favoritefood = models.CharField(max_length=100)
    favoritetoy = models.CharField(max_length=100)

    def __str__(self):
        return self.name