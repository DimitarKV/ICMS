from abc import abstractmethod
import math

from django.db import models

class Entity(models.Model):
    datetime_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class IceCream(Entity):
    name = models.CharField(max_length=255)
    height = models.FloatField()
    width = models.FloatField()

    def _get_radius(self):
        return self.width / 2

    @abstractmethod
    def get_volume():
        pass

class IceCreamCone(IceCream):
    def get_volume(self):
        return math.pi * (self._get_radius()**2) * self.height / 3

class IceCreamPrism(IceCream):
    def get_volume(self):
        return self.height * self.width**2

class IceCreamAvailability(Entity):
    ice_cream = models.ForeignKey("IceCream", on_delete=models.CASCADE)
    fridge = models.ForeignKey("Fridge", on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Fridge(Entity):
    floor = models.IntegerField()
    number_on_floor = models.IntegerField()
    description = models.CharField(max_length=511)
    volume = models.FloatField()

class Favorite(Entity):
    dev = models.ForeignKey("Person", on_delete=models.CASCADE)
    ice_cream = models.ForeignKey("IceCream", on_delete=models.CASCADE)

class Person(Entity):
    token = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    role = models.CharField(max_length=15)
    notification_settings = models.BooleanField(default=False)
    current_floor = models.IntegerField(null=True, default=None)