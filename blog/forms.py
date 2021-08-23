# from django import forms

from django import forms


class ShareForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(required=False)
    to = forms.EmailField(required=False)
    description = forms.CharField(
        widget=forms.Textarea,
        max_length=250,
        required=False)
