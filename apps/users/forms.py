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

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if username:
            username = username.strip()
            if " " in username:
                raise forms.ValidationError("Username can't have spaces")
            else:
                return username

    def clean_password_confirm(self):
            password = self.cleaned_data.get('password')
            password_confirm = self.cleaned_data.get('password_confirm')

            if password and password_confirm:
                if password != password_confirm:
                    raise forms.ValidationError("Passwords do not match")
                else:
                    return password_confirm