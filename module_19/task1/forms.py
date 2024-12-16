from django import forms
from django.core.exceptions import ValidationError
from .models import Buyer


class UserRegister(forms.Form):

    username = forms.CharField(max_length=30, label='Введите логин ',
                               error_messages={'required': 'Повторите попытку.'})

    password = forms.CharField(min_length=8, label=' Введите пароль ',
                               error_messages={'required': 'Повторите попытку.'},
                               widget=forms.PasswordInput())

    repeat_password = forms.CharField(min_length=8, label=' Повторите пароль ',
                                      error_messages={'required': 'Повторите попытку.'},
                                      widget=forms.PasswordInput())

    age = forms.IntegerField(min_value=18, label='Введите свой возраст',
                             error_messages={'required': 'Вы должны быть старше 18.', })

    def clean_username(self):
        data = self.cleaned_data["username"]
        users = Buyer.objects.all()
        for user in users:
            user = str(user)
            if data == user:
                raise ValidationError(f"Пользователь {data} уже зарегестрирован.")
        return data

    def clean(self):
        cleanet_danta = super().clean()
        passwd = self.cleaned_data["password"]
        rep_pass = self.cleaned_data["repeat_password"]
        if passwd != rep_pass:
            raise ValidationError("Пароли не совпадают")
        return cleanet_danta

    def clean_age(self):
        age = self.cleaned_data["age"]
        if len(str(age)) > 3:
            raise ValidationError("Введите корректный возраст")
        return int(age)


