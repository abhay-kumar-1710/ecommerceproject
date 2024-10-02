from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from ecommerceapp.models import Customer

class LogInForm(AuthenticationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'password']

class RegisterForm(UserCreationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.CharField(label="Email", widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Old Password", widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    new_password1 = forms.CharField(label="New Password", widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    new_password2 = forms.CharField(label="Confirm New Password", widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    class Meta:
        model = User
        fields = ['old_password', 'new_password1','new_password2']

class MyPasswordRestForm(PasswordResetForm):
    email = forms.CharField(label="Email", widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    class Meta:
        model = User
        fields = ['email']

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label="New Password", widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    new_password2 = forms.CharField(label="Confirm New Password", widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']

class CustomerForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    locality = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    # state = forms.CharField(widget=forms.Select(attrs={'class' : 'form-control'}))
    zipcode = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    class Meta:
        model = Customer
        fields = ['name', 'locality', 'city', 'state', 'zipcode']
        widgets = {
            'state'  : forms.Select(attrs={'class' : 'form-control'})
        }
