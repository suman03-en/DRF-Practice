from rest_framework import serializers
from .models import Product

def validate_title(value):
    qs = Product.objects.filter(title__iexact=value)
    if qs.exists():
        raise serializers.ValidationError("error")
    return value

class ValidateTitleMixin:
    def validate_title(self, value):
        model_class = self.Meta.model
        qs = model_class.objects.filter(title__exact=value)
        if qs.exists():
            raise serializers.ValidationError("error with mixins")
        return value