from django import forms

from main.models import Student


class StudentForm(forms.ModelForm):
    """
     Создает формы
    """

    class Meta:
        """
        Определяет параметры формы
        """
        model = Student

        # используется какой-то один параметр
        # fields = '__all__'  # выводит в форму все поля
        fields = ('first_name', 'last_name',)  # выводит в форму указанные поля
        # exclude = ('is_active',)  # выводит в форму все поля, кроме указанного

