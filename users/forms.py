from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import User
from django import forms


class UserRegisterForm(UserCreationForm):
    """

    """
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    """

    """
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar')

    def __init__(self, *args, **kwargs):
        """
        Дополнительные настройки
        """
        super().__init__(*args, **kwargs)

        # Позволяет не выводить в профиле поле пароля
        self.fields['password'].widget = forms.HiddenInput()

        # передаем в шаблон контроль формы
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
