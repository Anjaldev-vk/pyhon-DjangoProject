from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Decimal field for price
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.name
