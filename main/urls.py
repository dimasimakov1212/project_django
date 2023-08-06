from django.urls import path, include

from main.views import index_2, contact

urlpatterns = [
    path('', index_2),
    path('contact/', contact),
]
