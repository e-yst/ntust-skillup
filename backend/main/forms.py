from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class SignupForm(forms.Form):

    name = forms.CharField(
        max_length=100,
        label='使用者名稱',
        widget=forms.TextInput(attrs={
            'placeholder': '請輸入使用者名稱',
            'class': 'form-control',
            'aria-describedby': 'sizing-addon1'})
    )

    mail = forms.CharField(
        max_length=150,
        label='電子郵箱',
        widget=forms.TextInput(attrs={
            'placeholder': '請輸入電子郵箱',
            'class': 'form-control',
            'type': 'email',
            'aria-describedby': 'sizing-addon2'})
    )

    password = forms.CharField(
        max_length=50,
        label='密碼',
        widget=forms.TextInput(attrs={
            'placeholder': '請輸入密碼',
            'class': 'form-control',
            'type': 'password',
            'aria-describedby': 'sizing-addon3',
            'id': 'pass'})
    )

    pass_confirm = forms.CharField(
        max_length=50,
        label='確認密碼',
        widget=forms.TextInput(attrs={
            'placeholder': '確認密碼',
            'class': 'form-control',
            'type': 'password',
            'aria-describedby': 'sizing-addon4',
            'id': 'confirmPass'})
    )

    gender = forms.ChoiceField(
        choices=((0, '男'), (1, '女')),
        label='性別')

    date_of_birth = forms.DateField(
        label='生日',
        widget=forms.TextInput(attrs={
            'class':'datepicker',
        })
    )

    user_bio = forms.CharField(
        label='自我介紹',
        required=False,
        widget=forms.Textarea(attrs={
            'id': "bio",
            'rows': 3
        })
    )

    interests = forms.MultipleChoiceField(
        label='興趣',
        required=False,
        choices=(('develop', 'Development'), ('design', 'Design'),
                 ('business', 'Business')),
        widget=forms.CheckboxSelectMultiple()
    )

    def clean(self):
        username = self.cleaned_data['name']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        pass_confirm = self.cleaned_data['pass_confirm']

        try:
            u = User.objects.get(username=username)
            if u is not None:
                raise DuplicatedInfoException("duplicated usernames!")
        except DuplicatedInfoException:
            self.add_error('name', '使用者名稱已被使用')
        except User.DoesNotExist:
            pass

        try:
            u = User.objects.get(email=email)
            if u is not None:
                raise DuplicatedInfoException("duplicated email!")
        except DuplicatedInfoException:
            self.add_error('email', 'Email已被使用')
        except User.DoesNotExist:
            pass

        if password != password2:
            self.add_error('password2', '密碼不一致！')
