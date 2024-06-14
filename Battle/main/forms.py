"""
Файл для работы с формами
"""

from django import forms


class LoginForm(forms.Form):
    """Устанавливает поля рецептов"""
    login = forms.CharField(max_length=100)
    pswrd = forms.CharField(max_length=100)