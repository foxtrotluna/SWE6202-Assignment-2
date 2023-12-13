# Define the models

from django.db import models
from django.contrib.auth.models import User

class cardInfo(models.Model):
  # might be better for Luna to set this up as she's done some cards relating to the payment process
  pass

class Profile(models.Model):
  # link profile to default user model which stores username, password, email ect.
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  cardInfo = models.ForeignKey(cardInfo, on_delete=models.SET_NULL, null=True)

class Product(models.Model):
  price = models.FloatField(null=True)
  name = models.CharField(max_length=255, null=True)

class Basket(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, null=True)

class Order(models.Model):
  # 'do_nothing' because we still want the order to be stored in history even if the product is no longer being offered
  product = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, null=True)
  quantity = models.IntegerField()
  basket = models.ForeignKey(Basket, on_delete=models.DO_NOTHING, null=True)

class Review(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  stars = models.IntegerField()
  review = models.CharField(max_length=1600)

