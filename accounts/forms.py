from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()
class RegisterForm(forms.Form):
    email = forms.EmailField(
            widget=forms.TextInput(
            attrs=
            {
                "class": "form-control"
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    'class': 'form-control'
                }
        )
    )
    confirmation_password = forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    'class': 'form-control'
                }
        )
    )
    #this function is overridden
    def clean(self):
        pass1 = self.cleaned_data.get('password')
        pass2 = self.cleaned_data.get('confirmation_password')
        if pass1 != pass2:
            raise forms.ValidationError("passwords don't match")
        return self.cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = User.objects.filter(username=username)
        if user.exists():
            raise forms.ValidationError('user exists')
        return self.cleaned_data.get('username')

class LoginForm(forms.Form):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
          attrs={
            'class': 'form-control'
            
        }  
    )    
)
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    def clean_user(self):
        username = self.cleaned_data.get('username')
        user = User.objects.filter(username=username)
        if user is None:
            raise forms.ValidationError("this user doesn't exist")
        return self.cleaned_data['username']