from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name ="product-detail",
        lookup_field = "pk"
    )

    class Meta:
        model = Product
        fields = [
            'url',
            'title',
            'content',
            'price'
        ]
    # def get_url(self, obj):
    #     request = self.context.get("request")
    #     return reverse("product-detail",request=request, kwargs={"pk": obj.pk})
    