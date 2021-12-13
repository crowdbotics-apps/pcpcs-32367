from django.conf import settings
from django.db import models


class Discount(models.Model):
    "Generated Model"
    medical = models.BooleanField()
    military = models.BooleanField()
    educational = models.BooleanField()
