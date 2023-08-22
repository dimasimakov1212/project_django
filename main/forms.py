from django import forms

from main.models import Student, Subject


class StudentForm(forms.ModelForm):
    """
     Создает форму для заполнения даннных студента
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


class SubjectForm(forms.ModelForm):
    """
    Создает форму для заполнения даннных предмета
    """
    class Meta:
        model = Subject
        fields = '__all__'
