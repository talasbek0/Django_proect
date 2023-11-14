from django import forms
from .models import Review


class UserForm(forms.Form):
    name = forms.CharField()
    money = forms.IntegerField


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'text', 'rating']
