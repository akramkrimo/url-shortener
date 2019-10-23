from django import forms


class Shortener(forms.Form):
    url = forms.URLField(
        label='',
        widget=forms.URLInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter URL'
            }
        )
    )
