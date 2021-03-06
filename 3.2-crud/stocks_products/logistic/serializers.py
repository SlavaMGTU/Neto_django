from rest_framework import serializers

from logistic.models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    # настройте сериализатор для продукта
    class Meta:
        model = Product
        fields = ('title', 'description')


class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе
    class Meta:
        model = StockProduct
        fields = ('id', 'product', 'quantity', 'price')


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)
    #id = serializers.IntegerField()
    # настройте сериализатор для склада
    class Meta:
        model = Stock
        fields = ('id', 'address', 'positions')


    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        # создаем склад по его параметрам
        # здесь вам надо заполнить связанные таблицы в нашем случае: таблицу StockProduct с помощью списка positions
        stock = super().create(validated_data)
        for position in positions: #stock=stock_id,
            StockProduct.objects.create(stock=stock, **position)
            #product_id=position['product'], price=position['price'], quantity=position['quantity'])
                                       # defaults = {'price'=position['price'], 'quantity'=position['quantity']})
        #**position)#product=position['product'], price=position['price'], quantity=position['quantity'])
        #    StockProduct.objects.create(position) #position=position
        #     StockProduct.objects.create(stock('id'), position)
        #StockProduct.objects.create(positions)
            # quantity = position.pop('quantity')
            # price= position.pop('price')
            # StockProduct.objects.create(quantity=quantity, price=price)
        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)
        StockProduct.objects.filter(stock=stock).delete()
        # здесь вам надо обновить связанные таблицы в нашем случае: таблицу StockProduct с помощью списка positions
        for position in positions:
            StockProduct.objects.create(stock=stock, **position)
            # stockProduct=StockProduct.objects(id=position['product'], price=position['price'], quantity=position['quantity'])
            # stockProduct.save()
        return stock
