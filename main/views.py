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

    return render(request, 'main/contact.html')


def index_2(request):
    stud_list = Student.objects.all()
    context = {
        'object_list': stud_list
    }
    for student in stud_list:
        print(student)

    return render(request, 'main/test_html.html', context)
