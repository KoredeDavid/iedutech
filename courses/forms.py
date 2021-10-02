from django import forms

from .models import NewsLetter


class NewsLetterForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control  ', 'placeholder': 'Name'}))
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control  ', 'placeholder': 'Email'}))

    class Meta:
        model = NewsLetter
        fields = '__all__'
