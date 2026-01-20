from django.db import models
from django.db.models import Q
from django.conf import settings


User = settings.AUTH_USER_MODEL

class ProductQueryset(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)
    
    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()  
        return qs
    
class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQueryset(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query)
    

class Product(models.Model):
    user = models.ForeignKey(User, null=True, related_name="products", on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=15,decimal_places=2, default=99.99)
    public = models.BooleanField(default=True)


    #model manager
    objects = ProductManager()

    def __str__(self):
        return f"{self.title[:30]}"

    
