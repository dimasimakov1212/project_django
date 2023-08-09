from django.shortcuts import render
from django.views.generic import ListView, DetailView

from main.models import Student


class StudentListView(ListView):
    """
    Выводит информаццию о всех студентах на главную страницу вместо функции index_2
    """

    model = Student
    template_name = 'main/test_html.html'


class StudentDetailView(DetailView):
    """
    Выводит информаццию об одном, выбранном на главной странице, студенте вместо функции view_student
    """
    model = Student
    template_name = 'main/view_student.html'


def contact(request):
    """
    Выводит страницу с контактами и получает обратную связь
    """

    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        # а также передается информация, которую заполнил пользователь
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'Имя - {name}, почта - {email}, сообщение - {message}')

    context = {
        'title': 'Контакты'
    }

    return render(request, 'main/contact.html', context)


# def index_2(request):
#     """
#     Выводит информаццию о всех студентах на главную страницу
#     """
#     stud_list = Student.objects.all()
#     context = {
#         'object_list': stud_list,
#         'title': 'Главная'
#     }
#     for student in stud_list:
#         print(student)
#
#     return render(request, 'main/test_html.html', context)


# def view_student(request, pk):
#     """
#     Выводит информаццию об одном, выбранном на главной странице, студенте
#     """
#
#     student_info = Student.objects.get(pk=pk)  # получаем данные студента по его id
#     context = {
#         'student_info': student_info,
#         'title': 'Данные студента'
#     }
#
#     return render(request, 'main/view_student.html', context)
