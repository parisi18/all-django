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