from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from main.forms import StudentForm
from main.models import Student


class StudentListView(ListView):
    """
    Выводит информаццию о всех студентах на главную страницу вместо функции index_2
    """

    model = Student
    # template_name = 'main/student_list.html'

    # def get_context_data(self, **kwargs):
    #
    #     context = super().get_context_data(**kwargs)
    #     print(context)
    #
    #     return context


class StudentDetailView(DetailView):
    """
    Выводит информаццию об одном, выбранном на главной странице, студенте вместо функции view_student
    """
    model = Student
    # template_name = 'main/student_detail.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        print(context)

        return context


class StudentCreateView(CreateView):
    """
    Контроллер создания нового студента
    """
    model = Student
    # fields = ('first_name', 'last_name', 'avatar')  # если определен форм-класс, то поле не используется
    form_class = StudentForm
    success_url = reverse_lazy('main:test_html')


class StudentUpdateView(UpdateView):
    """
    Контроллер редактирования студента
    """
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('main:test_html')


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


def toggle_activity(request, pk):
    """
    Меняет статус студента (учится или нет)
    """
    student_item = get_object_or_404(Student, pk=pk)
    if student_item.is_active:
        student_item.is_active = False
    else:
        student_item.is_active = True

    student_item.save()

    return redirect(reverse('main:test_html'))

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
#     return render(request, 'main/student_list.html', context)


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
#     return render(request, 'main/student_detail.html', context)
