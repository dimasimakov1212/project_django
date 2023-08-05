from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Student(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='имя')
    last_name = models.CharField(max_length=150, verbose_name='фамилия')
    avatar = models.ImageField(upload_to='students/', verbose_name='аватар', **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name='учится')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'студент'  # Настройка для наименования одного объекта
        verbose_name_plural = 'студенты'  # Настройка для наименования набора объектов
        ordering = ('last_name',)  # сортировка по фамилии
