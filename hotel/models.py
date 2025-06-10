from django.db import models
from common.models import BaseDateTimeModel


class HotelCategory(BaseDateTimeModel):
    name = models.CharField(max_length=150, unique=True, primary_key=True)
    cat_index = models.IntegerField(default=0)

    def __repr__(self):
        return self.name


class HotelDetail(BaseDateTimeModel):
    short_id = models.CharField(max_length=250, unique=True, primary_key=True)
    name = models.CharField(max_length=250)
    address_line_1 = models.CharField(max_length=250)
    address_line_2 = models.CharField(blank=True, null=True, max_length=250)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    pincode = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    fecilities = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(HotelCategory, on_delete=models.CASCADE, blank=True, null=True)

    def __repr__(self):
        return self.short_id
