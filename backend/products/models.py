from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Product(models.Model):
    user = models.ForeignKey(User, related_name="products", on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=15,decimal_places=2, default=99.99)


    def __str__(self):
        return f"{self.title[:30]}"

    
