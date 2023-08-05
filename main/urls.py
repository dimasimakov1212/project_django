from django.urls import path, include

from main.views import index_2

urlpatterns = [
    path('', index_2),
]
