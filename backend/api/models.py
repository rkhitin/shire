from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class CustomerSettings(models.Model):
    PRIVATE = 'PR'
    PUBLIC = 'PB'
    PRIVACY_LEVEL = (
        (PRIVATE, 'Личный'),
        (PUBLIC, 'Публичный'),
    )

    customer = models.OneToOneField(
        Customer, related_name='settings', on_delete=models.CASCADE)
    privacy_level = models.CharField(
        max_length=2,
        choices=PRIVACY_LEVEL,
        default=PRIVATE,
    )


class Category(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7)
    icon_name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Obstacle(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Habbit(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    category = models.OneToOneField(
        Category, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    wish = models.TextField()
    outcome = models.TextField()
    obstacles = models.ManyToManyField(Obstacle)

    def __str__(self):
        return self.title


class OvercomePlan(models.Model):
    obstacle = models.OneToOneField(Obstacle, on_delete=models.CASCADE)
    text = models.TextField()
