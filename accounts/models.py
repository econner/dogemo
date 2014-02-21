from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    friends = models.ManyToManyField("self")
    phone = models.CharField(max_length=20, unique=True)


class Transaction(models.Model):
    to_user = models.ForeignKey(User, related_name="received_transactions")
    to_phone = models.CharField(max_length=20)
    # http://isemail.info/about
    to_email = models.CharField(max_length=254)
    from_user = models.ForeignKey(User, related_name="sent_transactions")
    amount = models.FloatField()  # TODO better representation
    created_at = models.DateTimeField()
    status = models.CharField(max_length=10)  # TODO enum


class Address(models.Model):
    address = models.CharField(max_length=34)
    owner = models.ForeignKey(User)