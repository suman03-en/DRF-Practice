from rest_framework import serializers
from rest_framework.reverse import reverse

from .validators import validate_title, ValidateTitleMixin
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name ="product-detail",
        lookup_field = "pk"
    )
    # email = serializers.EmailField(write_only=True)

    class Meta:
        model = Product
        fields = [
            'url',
            'title',
            'content',
            'price'
        ]


    def validate_price(self, value):
        """
        Field level validation
        """
        if value < 0:
            raise serializers.ValidationError(f"price cannot be negative.")
        return value
    
    def validate(self, attrs):
        """
        Object level validation, called after all validation_fields.
        """
        title = attrs.get("title")
        content = attrs.get("content")
        if not content:
            updated = "Automatic: " + title
            attrs["content"] = updated
        return super().validate(attrs)
    
    
    def create(self, validated_data):
        user = self.context.get("request").user
        validated_data["user"] = user
        return super().create(validated_data)

    
    # def create(self,validated_data):
    #     email = validated_data.pop("email")
    #     print(email)
    #     return super().create(validated_data)
    
    # def update(self, instance, validated_data):
    #     email = validated_data.pop("email")
    #     return super().update(instance, validated_data)

    # def get_url(self, obj):
    #     request = self.context.get("request")
    #     return reverse("product-detail",request=request, kwargs={"pk": obj.pk})
    