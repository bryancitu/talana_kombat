from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Player(BaseModel):
    """Model definition for Player."""

    full_name = models.CharField(
        'Nombre del personaje', 
        max_length=50
    )
    username = models.CharField(
        _('username'), 
        max_length=254, 
        unique=True
    )

    class Meta:
        """Meta definition for Player."""

        verbose_name = 'Player'
        verbose_name_plural = 'Players'

    def __str__(self):
        """Unicode representation of Player."""
        return self.full_name

class Power(BaseModel):
    """Model definition for Power."""

    player = models.ForeignKey(
        Player, 
        default=None, 
        related_name='player', 
        on_delete=models.CASCADE
    )
    name = models.CharField(
        'Nombre del movimiento',
        max_length=20
    )
    combination = models.CharField(
        _('combination'),
        max_length=6
    )
    energy = models.IntegerField(
        'Energía que quita'
    )

    class Meta:
        """Meta definition for Power."""

        verbose_name = 'Power'
        verbose_name_plural = 'Powers'

    def __str__(self):
        """Unicode representation of Power."""
        return self.name
