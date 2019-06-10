from django import forms
class RegistrationForm(forms.Form):
    first_name=forms.CharField(
        label="Enter first name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'firstname'
            }
        )
    )
    last_name=forms.CharField(
        label="Enter last name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'lastname',

            }
        )
    )
    user_name=forms.CharField(
        label="Enter user name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'user_name',
            }
        )
    )
    password1=forms.CharField(
        label="Enter your password",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'password1'
            }
        )
    )
    password2=forms.CharField(
        label="Enter confirm password",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'confirm password'
            }

        )
    )
    email = forms.EmailField(
        label="Enter your Email",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Emailid'
            }

        )
    )
    number = forms.IntegerField(
        label="Enter your number",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder':'Mobilenumber'
            }

        )
    )
class LoginForm(forms.Form):
    user_name=forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'User_name'
            }
        )

    )
    password1=forms.CharField(
        label="Enter your password",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'password1'
            }
        )
    )