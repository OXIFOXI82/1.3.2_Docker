from rest_framework import serializers

from .models import Product,Stock,StockProduct


class ProductSerializer(serializers.ModelSerializer):
    # настройте сериализатор для продукта
    class Meta:
      model=Product
      fields= ['id', 'title', 'description']



class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']
        # depth=1



class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)
    class Meta:
         model=Stock

         fields=['address','positions']


    def create(self, validated_data):
            positions = validated_data.pop('positions')
            stock = super().create(validated_data)

            for position in positions:
                StockProduct.objects.create(stock=stock, **position)
            return stock



    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')

        stock = super().update(instance, validated_data)

        for position in positions:
            StockProduct.objects.update_or_create(defaults={'quantity': position['quantity'], 'price': position['price']},
                                                  product=position['product'], stock=stock)
        return stock
