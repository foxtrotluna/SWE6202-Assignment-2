# Define the models

from django.db import models

class User(models.Model):
  isAdmin = models.BooleanField()

class Seller(models.Model):
  address = models.CharField(max_length=255)

class Payment(models.Model):
  paid = models.BooleanField()

class Product(models.Model):
  name = models.CharField(max_length=75)

class Category(models.Model):
  name = models.CharField(max_length=50)

class Order(models.Model):
  totalAmount = models.IntegerField()

class ShoppingCart(models.Model):
  createdDate = models.DateField()

class Customer(models.Model):
  email = models.CharField(max_length=255)

class ShoppingInfo(models.Model):
  shippingCost = models.IntegerField()