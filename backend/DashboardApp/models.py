from django.db import models

class Firm(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100)
    Firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)


class Transaction(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
