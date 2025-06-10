from django.db import models
from common.models import BaseDateTimeModel


class RoomCategory(BaseDateTimeModel):
    name = models.CharField(max_length=100, unique=True, blank=True)
    cat_index = models.IntegerField(default=0)

    def __repr__(self):
        return self.name


class RoomInfo(models.Model):
    room_number = models.CharField(max_length=50)
    floor = models.CharField(max_length=100)
    room_type = models.ForeignKey(RoomCategory, on_delete=models.CASCADE, blank=True, null=True)
    description = models.CharField(blank=True, null=True)
    hotel = models.ForeignKey("hotel.HotelCategory", on_delete=models.CASCADE, blank=True, null=True)
    price_per_night = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    max_occupation = models.IntegerField(default=1)
    features = models.TextField(blank=True, null=True)
    available = models.BooleanField(default=False)

    def __repr__(self):
        return self.room_number