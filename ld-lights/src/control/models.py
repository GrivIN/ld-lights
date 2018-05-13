from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Light(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    address = models.GenericIPAddressField(default='192.168.178.42')
    port = models.PositiveSmallIntegerField(default=8899)

    red = models.PositiveSmallIntegerField(
        default=255,
        validators=[
            MaxValueValidator(255),
            MinValueValidator(0)
        ]
    )
    green = models.PositiveSmallIntegerField(
        default=255,
        validators=[
            MaxValueValidator(255),
            MinValueValidator(0)
        ]
    )
    blue = models.PositiveSmallIntegerField(
        default=255,
        validators=[
            MaxValueValidator(255),
            MinValueValidator(0)
        ]
    )

    is_on = models.BooleanField(default=False)

    class Meta:
        unique_together = ('address', 'port')

    def __str__(self):
        return self.name
