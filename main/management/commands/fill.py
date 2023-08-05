from django.core.management import BaseCommand

from main.models import Student


class Command(BaseCommand):

    def handle(self, *args, **options):
        st_list = [
            {'last_name': 'Пупкин', 'first_name': 'Пу'},
            {'last_name': 'Ножкин', 'first_name': 'Но'},
            {'last_name': 'Ручкин', 'first_name': 'Ру'}
        ]

        # for student in st_list:
        #     Student.objects.create(**student)

        st_for_create = []
        for student in st_list:
            st_for_create.append(Student(**student))

        # print(st_for_create)

        Student.objects.bulk_create(st_for_create)
