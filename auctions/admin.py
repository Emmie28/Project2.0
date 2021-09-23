from django.contrib import admin
from .models import Auction, Bidding, WatchList, Comment


# Register your models here.
admin.site.register(Auction)
admin.site.register(Bidding)
admin.site.register(WatchList)
admin.site.register(Comment)
