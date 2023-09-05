from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.cache import cache

from config import settings
from main.forms import StudentForm, SubjectForm
from main.models import Student, Subject

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required

from main.services import get_cached_subjects_for_student


class StudentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    Выводит информаццию о всех студентах на главную страницу вместо функции index_2
    """

    model = Student
    permission_required = 'main.view_student'  # проверка прав доступа

    # template_name = 'main/student_list.html'

    # def get_context_data(self, **kwargs):
    #
    #     context = super().get_context_data(**kwargs)
    #     print(context)
    #
    #     return context


class StudentDetailView(LoginRequiredMixin, DetailView):
    """
    Выводит информаццию об одном, выбранном на главной странице, студенте вместо функции view_student
    """
    model = Student

    # template_name = 'main/student_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # subject_list = self.object.subject_set.all()

        # функционал перенесен в файл services.py
        # if settings.CACHE_ENABLED:
        #     key = f'subject_list_{self.object.pk}'  # ключ, по которому получаем список предметов
        #     subject_list = cache.get(key)  # получаем все предметы студента
        #     if subject_list is None:
        #         subject_list = self.object.subject_set.all()
        #         cache.set(key, subject_list)  # кэшируем список предметов
        # else:
        #     subject_list = self.object.subject_set.all()

        context['subjects'] = get_cached_subjects_for_student(self.object.pk)

        return context


class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    Контроллер создания нового студента
    """
    model = Student
    # fields = ('first_name', 'last_name', 'avatar')  # если определен форм-класс, то поле не используется
    form_class = StudentForm
    permission_required = 'main.add_student'
    success_url = reverse_lazy('main:test_html')

    def get_context_data(self, **kwargs):
        """
        Добавляем формы для внесения данных о предметах студента
        """
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Student, Subject, form=SubjectForm, extra=1)

        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        """
        Проверяем данные на правильность заполнения
        """
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    Контроллер редактирования студента
    """
    model = Student
    form_class = StudentForm
    permission_required = 'main.change_student'
    success_url = reverse_lazy('main:test_html')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Student, Subject, form=SubjectForm, extra=1)

        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class StudentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    Выводит форму удаления материала
    """
    model = Student
    permission_required = 'main.delete_student'
    success_url = reverse_lazy('main:test_html')


@login_required
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
