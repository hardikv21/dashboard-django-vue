from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from DashboardApp.views import FirmViewSet, UserViewSet, ProductViewSet, TransactionViewSet
from DashboardApp.serializers import FirmSerializer, UserSerializer, ProductSerializer, TransactionSerializer
from DashboardApp.models import Firm, User, Product, Transaction
from DashboardApp.test_data import testData


class FirmViewSetTest(APITestCase):
    def setUp(self):
        testData(self)

    def test_list(self):      
        url = reverse("firm-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = FirmSerializer(Firm.objects.all(), many=True)
        self.assertEqual(response.data, data.data)


class UserViewSetTest(APITestCase):
    def setUp(self):
        testData(self)

    def test_list(self):      
        url = reverse("user-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = UserSerializer(User.objects.all(), many=True)
        self.assertEqual(response.data, data.data)


class ProductViewSetTest(APITestCase):
    def setUp(self):
        testData(self)

    def test_list(self):      
        url = reverse("product-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = ProductSerializer(Product.objects.all(), many=True)
        self.assertEqual(response.data, data.data)


class TransactionViewSetTest(APITestCase):
    def setUp(self):
        testData(self)        

    def test_list(self):      
        url = reverse("transaction-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = TransactionSerializer(Transaction.objects.all(), many=True)
        self.assertEqual(response.data, data.data)
