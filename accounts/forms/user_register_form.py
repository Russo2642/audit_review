from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from accounts.models import Department


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput,
        label='Введите пароль',
    )
    password_confirm = forms.CharField(
        required=True,
        widget=forms.PasswordInput,
        label='Подтвердите пароль',
    )
    department = forms.ModelMultipleChoiceField(
        queryset=Department.objects.all(),
        widget=forms.Select,
        label='Департамент',
    )

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'first_name',
            'last_name',
            'password',
            'password_confirm',
            'department',
            'email',
        )
        labels = {
            'username': 'Логин',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Почта руководителя департамента',
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password_confirm and password and password != password_confirm:
            raise ValidationError('')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))

        if commit:
            user.save()
        return user
