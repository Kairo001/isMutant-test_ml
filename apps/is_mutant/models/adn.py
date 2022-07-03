# Django
from django.db import models

class Adn(models.Model):
  """Model definition for Adn."""

  adn = models.TextField(unique=True)
  is_mutant = models.BooleanField()

  class Meta:
    """Meta definition for Adn."""

    verbose_name = 'Adn'
    verbose_name_plural = 'Adns'

  def __str__(self):
    """Unicode representation of Adn."""
    return self.is_mutant
