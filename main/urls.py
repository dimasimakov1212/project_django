from django.urls import path, include

from main.apps import MainConfig
from main.views import index_2, contact, view_student

app_name = MainConfig.name

urlpatterns = [
    path('', index_2, name='test_html'),
    path('contact/', contact, name='contact'),
    path('<int:pk>/view_student', view_student, name='view_student'),

]
