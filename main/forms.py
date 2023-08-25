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
        fields = ('first_name', 'last_name', 'email')  # выводит в форму указанные поля
        # exclude = ('is_active',)  # выводит в форму все поля, кроме указанного

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_email(self):
        """
        Проверяет корректность ввода email
        """
        cleaned_data = self.cleaned_data['email']

        if 'sky.pro' not in cleaned_data:
            raise forms.ValidationError('Почта должна относиться к учебному заведению')

        return cleaned_data


class SubjectForm(forms.ModelForm):
    """
    Создает форму для заполнения даннных предмета
    """
    class Meta:
        model = Subject
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
