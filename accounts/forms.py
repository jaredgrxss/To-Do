from attr import attr
from django import forms 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField


class UserCreateForm(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = ('username','email','password1','password2')
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Username"
        self.fields['password1'].label = "Create Password"
        self.fields['password2'].label = "Verify Password"

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'login-user',
            'type':'text',
            'placeholder':'Enter a username!',
        }
    ))
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'login-email',
            'type':'email',
            'placeholder':'Enter your email!',
        }
    ))
    password1 = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'login-pass',
            'type':'password',
            'placeholder':'Enter a password!',
        }
    ))
    password2 = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'login-pass',
            'type':'password',
            'placeholder':'Re-enter your password!',
        }
    ))


    


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.error_messages['invalid_login']
    
    username = UsernameField(widget=forms.TextInput(
        attrs= {
            'class':'login-user',
            'placeholder':'Enter your username',
            'id':'hello'
            }

    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs = {
            'class':'login-pass',
            'placeholder':'Enter your password',
            'id':'',
        }
    ))

