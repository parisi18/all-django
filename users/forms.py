from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username', 
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Username'},
        )
    )

    password = forms.CharField(
        label='Password', 
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Password'}
        )
    )

class SubscribeForm(forms.Form):
    username = forms.CharField(
        label='Username', 
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Username'},
        )
    )

    email = forms.EmailField(
        label='Email', 
        required=True,
        widget=forms.EmailInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Email'}
        )
    )

    password = forms.CharField(
        label='Password', 
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Type your password'}
        )
    )

    password_confirm = forms.CharField(
        label='Password confirm', 
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Type your password again'}
        )
    )