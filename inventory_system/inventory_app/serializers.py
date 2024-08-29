from rest_framework import serializers
from .models import Product, Category, Sale

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['popularity_score', 'sales_count']

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['popularity_score', 'sales_count', 'inventory_count']


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

    def create(self, validated_data):
        product = validated_data['product']
        quantity = validated_data['quantity']
        if product.inventory_count < quantity:
            raise serializers.ValidationError("Not enough inventory to complete the sale")
        return super().create(validated_data)