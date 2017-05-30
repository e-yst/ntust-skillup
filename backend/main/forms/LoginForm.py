from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):

    name = forms.CharField(
        max_length=100,
        label='使用者名稱',
        widget=forms.TextInput(attrs={
            'placeholder': '使用者名稱',
            'class': 'form-control'})
    )

    password = forms.CharField(
        max_length=50,
        label='密碼',
        widget=forms.TextInput(attrs={
            'placeholder': '密碼',
            'class': 'form-control',
            'type': 'password'})
    )

    def clean(self):
        username = self.cleaned_data['name']
        password = self.cleaned_data['password']

        u = authenticate(username=username,
                         password=password)

        print(u)

        if u is None:
            self.add_error('password', '帳號或密碼不正確')
