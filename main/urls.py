from django.urls import path, include

from main.apps import MainConfig
from main.views import index_2, contact

app_name = MainConfig.name

urlpatterns = [
    path('', index_2, name='test_html'),
    path('contact/', contact, name='contact'),
]
