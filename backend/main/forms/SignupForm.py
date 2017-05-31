from django import forms
from django.contrib.auth.models import User
from django.utils import timezone

from main.models import Category

from datetime import datetime, timedelta
from pytz import timezone as tz


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

    dob = forms.CharField(
        label='生日',
        widget=forms.TextInput(attrs={
            'class':'datepicker',
            'placeholder': '點選此處選擇日期'
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
        choices=((c.id, c.name) for c in Category.objects.all()),
        widget=forms.CheckboxSelectMultiple()
    )

    def clean(self):
        username = self.cleaned_data['name']
        mail = self.cleaned_data['mail']
        password = self.cleaned_data['password']
        pass_confirm = self.cleaned_data['pass_confirm']
        dob = datetime.strptime(
            self.cleaned_data['dob'],
            '%Y/%m/%d'
        ).replace(tzinfo=tz('Asia/Taipei'))

        try:
            u = User.objects.get(username=username)
            if u is not None:
                raise DuplicatedInfoException("duplicated usernames!")
        except DuplicatedInfoException:
            self.add_error('name', '使用者名稱已被使用')
        except User.DoesNotExist:
            pass

        if password != pass_confirm:
            self.add_error('pass_confirm', '密碼不一致！')

        try:
            u = User.objects.get(email=mail)
            if u is not None:
                raise DuplicatedInfoException("duplicated email!")
        except DuplicatedInfoException:
            self.add_error('mail', 'Email已被使用')
        except User.DoesNotExist:
            pass

        if (timezone.now() - timezone.localtime(dob)).days < timedelta(365*16).days:
            self.add_error('dob', '使用者需年滿16歲')




class DuplicatedInfoException(Exception):
    pass
