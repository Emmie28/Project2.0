from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages

import datetime

from .models import User, Auction, Bidding, ListDetails, Comment, CATEGORIES
from .forms import ListForm, BiddingForm, CommentForm

watch_count = 0


def index(request):
    f = Auction.objects.all()
    return render(request, "auctions/index.html", {"form": f})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            # Make uname (username) a global variable.
            global uname
            uname = user.username
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


@login_required
def create_listing(request):

    if request.method == "POST":
        form = ListForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            category = form.cleaned_data.get('category')

            # Update the category list.
            CATEGORIES.append(category)

            # Get object by title.
            obj = Auction.objects.get(title=title)
            obj.date = timezone.now()
            obj.save()

            # Update the ListDetails model.
            details = ListDetails(listing=obj, listed_by=uname, date=timezone.now())
            details.save()
            messages.success(request, "Item added successfully.")
            return redirect('index')

    else:
        form = ListForm()

    return render(request, 'auctions/create.html', {'form': form})


def active_listing(request):

    f = Auction.objects.all()

    return render(request, 'auctions/active_listing.html', {'form': f})


def categories(request):
    cat_list = []
    for i in range(len(CATEGORIES)):
        cat_list.append(CATEGORIES[i][0])
    return render(request, 'auctions/category.html', {'categories': cat_list})


# To get an item with its category
def category_list(request, category):
    if request.method == 'POST':
        items = Auction.objects.filter(category=category)
        return render(request, 'auctions/cat_list.html',  {'category': items, 'cat_name': category})
    else:
        return HttpResponse('Get away')


# To handle item listings.

def listing(request, name):

    # A function to create and populate a list of comments.
    def populate_list(comments):
        # A list to hold all the comments
        l = []

        # populate the list with existing comments.
        for com in comments:
            l.append(com)
        return l

    # Declare and Initialise variables
    data_id = int(name)
    obj = Auction.objects.get(id=data_id)
    obj_price = obj.min_price

    details = ListDetails.objects.filter(listing=obj)
    form = BiddingForm()
    c_form = CommentForm()
    comments = Comment.objects.filter(tag=obj)

    l = populate_list(comments)

    # Get the number bids on an item.
    bid_count = Bidding.objects.filter(item=obj)
    count = len(bid_count)

    if request.method == 'POST':
        if request.POST.get('submit'):
            form = BiddingForm(request.POST)
        if form.is_valid():
            bid = form.cleaned_data.get('bid_amount')

            # Check if the bid is less than the minimum bid.
            if int(bid) < int(obj_price):
                messages.error(request, "Your bid is less than the minimum.")
                return render(request, "auctions/listing.html", {'name': obj, 'form': form, 'item': Bidding.item,
                                                    'details': details, 'c_form': c_form, 'comment': l,'count': count})
            else:
                bidding = Bidding(item=obj, bid_amount=bid, bidder_name=uname)
                bidding.save()
                bid_count = Bidding.objects.filter(item=obj)
                count = len(bid_count)
                messages.success(request, 'Your bid is the current bid.')
                return render(request, "auctions/listing.html", {'name': obj, 'form': form, 'item': Bidding.item,
                                                 'details': details, 'c_form': c_form, 'comment': l, 'count':count})

        # Get data from the comment form.
        data = request.POST.get('your_comment')
        if data:
            comments = Comment(comment=data, tag=obj, comment_by=uname, date=datetime.datetime.now())
            comments.save()
            comments = Comment.objects.filter(tag=obj)
            l = populate_list(comments)

            return render(request, "auctions/listing.html", {'name': obj, 'form': form, 'item': Bidding.item,
                                                    'details': details, 'c_form': c_form, 'comment': l, 'count':count})
        else:
            obj.delete()
            f = Auction.objects.all()
            return render(request, 'auctions/index.html', {'form': f})

    return render(request, "auctions/listing.html", {'name': obj, 'form': form, 'item': Bidding.item,
                                                     'details': details,'c_form': c_form, 'comment':l, 'count':count})


def add_watch_list(request, item):
    obj = Auction.objects.get(title=item)
    msg = ""

    # Add to the watchlist
    if 'add-to-watchlist' in request.POST:
        obj.watchlist = True
        msg += "Item added successfully."

    # Remove from the watchlist
    else:
        obj.watchlist = False
        msg = "Item deleted successfully."
    obj.save()

    obj = Auction.objects.all()
    messages.success(request, msg)
    return render(request, "auctions/watchlist.html", {'name': obj})


@login_required
def watchlist(request):
    watch_list = Auction.objects.all()
    return render(request, "auctions/watchlist.html", {'name': watch_list})


@login_required
def close_bid(request, name):

    if request.method == 'POST':
        item = Auction.objects.get(title=name)
        bid_items = Bidding.objects.filter(item=item)

        # A dictionary to hold the item with the corresponding bid amount.
        amt = {}

        for bid in bid_items:
            amt.update({bid.bidder_name: bid.bid_amount})

        sorted(amt.items())

        try:
            winner = amt.popitem()
            messages.success(request, f"{winner[0]} won the bid.")
            item.delete()
            return redirect('index')
        except Exception:
            return HttpResponse("Error occurred while trying to delete the item")

    else:
        return HttpResponse("Get Away. This is not a POST request.")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
