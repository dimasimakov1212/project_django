from django.shortcuts import render

from main.models import Student


def contact(request):
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


def index_2(request):
    stud_list = Student.objects.all()
    context = {
        'object_list': stud_list,
        'title': 'Главная'
    }
    for student in stud_list:
        print(student)

    return render(request, 'main/test_html.html', context)


def view_student(request, pk):

    student_info = Student.objects.get(pk=pk)  # получаем данные студента по его id
    context = {
        'student_info': student_info,
        'title': 'Главная'
    }

    return render(request, 'main/view_student.html', context)
