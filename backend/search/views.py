from rest_framework import generics
from products.serializers import ProductSerializer
from products.models import Product

class SearchListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.query_params.get("query")
        results = Product.objects.none()
        if query is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(query , user=user)
        return results

