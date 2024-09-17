import uuid
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 255)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()
    
    @property
    def is_available(self):
        return self.quantity > 0
"""
    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5
"""