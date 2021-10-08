from django import forms
from django.forms import ModelForm
from .models import *


class ListForm(ModelForm):
    class Meta:
        model = Auction
        exclude = ('watchlist', 'date',)
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'min_price': forms.TextInput(attrs={'class': 'form-control'}),
            'auction_image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={"rows": 10, "cols": 40}))


class CategoriesForm(forms.Form):
    category = forms.Select(choices=('Books', 'Fashion', 'Electronics', 'Accessories'))


class BiddingForm(forms.Form):
    bid_amount = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control'}))






