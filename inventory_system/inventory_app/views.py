from rest_framework import viewsets, filters
from .models import Product, Category, Sale
from .serializers import ProductSerializer, CategorySerializer, SaleSerializer, ProductListSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-popularity_score')
    serializer_classes = {
        'create': ProductSerializer
    }
    default_serializer_class = ProductListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'category__name']

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all().order_by('-sale_date')
    serializer_class = SaleSerializer
