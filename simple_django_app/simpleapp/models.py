from django.db import models


class Pet(models.Model):
    """
    A nice way to test different field types
    """
    CAT = "cat"
    DOG = "dog"
    BIRD = "bird"
    OTHER = "other"
    PET_TYPE_CHOICES = (
        (CAT, "🐱"),
        (DOG, "🐶"),
        (BIRD, "🐦"),
        (OTHER, "❓"),
    )

    name = models.CharField(max_length=120)
    birthday = models.DateField()
    type = models.CharField(
        max_length=8,
        choices=PET_TYPE_CHOICES,
        default=OTHER,
    )
    weight = models.DecimalField('Weight (Kg)', max_digits=5, decimal_places=2)

    # Following is useful for tracking/debugging
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name
