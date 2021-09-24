from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime


class User(AbstractUser):
    pass


CATEGORIES = (
    ('No Category','No Category'),
    ('Books', 'Books'),
    ('Fashion', 'Fashion'),
    ('Electronics', 'Electronics'),
    ('Accessories', 'Accessories'),
)


class Auction(models.Model):
    title = models.CharField(primary_key=False, max_length=200, default="Title")
    description = models.TextField(default="Description")
    auction_image = models.ImageField(upload_to="images/", blank=True, null=True)
    min_price = models.FloatField(default=0.00)
    watchlist = models.BooleanField(default=False)
    category = models.CharField(max_length=150, choices=CATEGORIES, default="No Category")
    date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.title


class WatchList(models.Model):
    title = models.CharField(primary_key=False, max_length=200, default="Title")
    description = models.TextField(default="Description")
    auction_image = models.ImageField(upload_to="images/", blank=True, null=True)
    min_price = models.FloatField(default=0.00)

    def __str__(self):
        return self.title


class ListDetails(models.Model):
    listing = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="list_item")
    listed_by = models.CharField(primary_key=False, max_length=100, default="")
    date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.listed_by


class Comment(models.Model):
    comment = models.TextField(primary_key=False, default="Comment")
    tag = models.ForeignKey(Auction, on_delete=models.CASCADE)
    comment_by = models.CharField(primary_key=False, max_length=200, default="Comment_by")
    date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.comment


class Categories(models.Model):
    item = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="item")
    category = models.CharField(max_length=200)


class Bidding(models.Model):
    item = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="bid_item")
    bidder_name = models.CharField(primary_key=False, max_length=200, default="Your name")
    bid_amount = models.CharField(primary_key=False, max_length=200, default="Bid_amount")

    def __str__(self):
        return self.bid_amount









