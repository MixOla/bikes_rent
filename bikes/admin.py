from django.contrib import admin

from authentication.models import User
from bikes.models import Bike, Rental

admin.site.register(Bike)
admin.site.register(Rental)
