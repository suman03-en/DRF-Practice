from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions

from django.shortcuts import get_object_or_404


from .models import Product
from .serializers import ProductSerializer
from .permissions import IsOwnerPermission
from api.mixins import StaffEditorPermissionMixin

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def perform_create(self, serializer):
    #     """Override this method to modify the serializer or obj before saving it"""

    #     user = self.request.user
    #     serializer.save(user=user)
    #     #this is the another way to add the user to the model


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerPermission]
    lookup_field = 'pk'

class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerPermission]


#can be done this way
product_detail_view = ProductDetailAPIView.as_view()
product_list_create_view = ProductListCreateAPIView.as_view()
product_update_view = ProductUpdateAPIView.as_view()
product_delete_view = ProductDeleteAPIView.as_view()


#function based api views
@api_view(["GET","POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    
    if method == "GET":
        #either list or get detail
        if pk is not None:
            #detail view
            obj = get_object_or_404(Product,pk=pk)
            data = ProductSerializer(obj).data
            return Response(data)
        
        #list view
        qeuryset = Product.objects.all()
        data = ProductSerializer(qeuryset, many=True).data
        return Response(data)


    if method == "POST":
        #create view
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"invalid":"not good data"},status=400)
    