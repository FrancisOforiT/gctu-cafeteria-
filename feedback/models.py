
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)  # Allow blank images
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def clean(self):
        if self.price < 0:
            raise ValidationError('Price cannot be negative.')

    @property
    def imageURL(self):
        if self.image:
            return self.image.url
        return ''


class Feedback(models.Model):
    FOOD_CHOICES = [
        ('Poor', 'Poor'),
        ('Average', 'Average'),
        ('Good', 'Good'),
        ('Excellent', 'Excellent'),
    ]

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    food = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    cleanliness = models.CharField(max_length=50)
    service_quality = models.CharField(max_length=50)
    menu_variety = models.CharField(max_length=50)
    comments = models.TextField(blank=True, null=True)
    rating = models.PositiveSmallIntegerField(default=5)  # From 1 to 5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Feedback from {self.user.username if self.user else "Anonymous"}'
