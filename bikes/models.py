from django.db import models

from authentication.models import User


class Bike(models.Model):
    model = models.CharField(max_length=100, default='Аист')
    serial_number = models.CharField(max_length=50, unique=True)
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Велосипед"
        verbose_name_plural = "Велосипеды"

    def __str__(self):
        return f"{self.model}"

class Rental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username} арендовал {self.bike} с {self.start_time} до {self.end_time}"

    class Meta:
        verbose_name = "Аренда"
        verbose_name = "Аренда велосипедов"




