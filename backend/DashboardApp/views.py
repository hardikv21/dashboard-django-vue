from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Prefetch

from DashboardApp.models import Firm, User, Product, Transaction
from DashboardApp.serializers import FirmSerializer, UserSerializer, ProductSerializer, TransactionSerializer


class FirmViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer

    def list(self, request):
        firms = Firm.objects.all()
        serializer = FirmSerializer(firms, many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class TransactionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def list(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    @action(
        detail=False,
        methods=["get"],
        url_name="user_transactions",
        url_path="user_transactions/(?P<user_pk>[^/.]+)",
    )
    def userTransactions(self, request, user_pk=None):
        transactions = Transaction.objects.filter(user=user_pk)
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

