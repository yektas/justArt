from django import forms
from django.contrib.auth.models import User
from django.forms import EmailInput, PasswordInput, TextInput


class RegistrationForm(forms.ModelForm):
    full_name = forms.CharField()
    password = forms.CharField()
    password2 = forms.CharField()
    email = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['full_name'].widget = TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Adınız ve Soyadınız'})
        self.fields['email'].widget = EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email adresiniz'})
        self.fields['password'].widget = PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Şifreniz'})
        self.fields['password2'].widget = PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Şifreyi tekrar giriniz'})

    class Meta:
        model = User
        fields = ('email', "password", "password2")

    def clean_full_name(self):
        cd = self.cleaned_data
        cd['first_name'], cd['last_name'] = cd['full_name'].split(' ')
        data = (cd['first_name'], cd['last_name'])
        return data

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def clean_email(self):
        cd = self.cleaned_data
        if User.objects.filter(email=cd["email"]).exists():
            raise forms.ValidationError("Bu email ile daha önce kayıt olunmuş.")
        return cd["email"]


class LoginForm(forms.ModelForm):
    email = forms.CharField()
    password = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget = EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email adresiniz'})
        self.fields['password'].widget = PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Şifreniz'})

    class Meta:
        model = User
        fields = ["email", "password"]
