from rest_framework import serializers
from DashboardApp.models import Firm, User, Product, Transaction


class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = '__all__'

        
class UserSerializer(serializers.ModelSerializer):
    Firm = FirmSerializer(many=False)

    class Meta:
        model = User
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    Product = ProductSerializer(many=False)
    user = UserSerializer(many=False)

    class Meta:
        model = Transaction
        fields = '__all__'
