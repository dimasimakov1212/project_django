from django.urls import path, include

from main.apps import MainConfig
from main.views import contact, StudentListView, StudentDetailView

app_name = MainConfig.name

urlpatterns = [
    # path('', index_2, name='test_html'),
    path('', StudentListView.as_view(), name='test_html'),
    path('contact/', contact, name='contact'),
    # path('view_student/<int:pk>/', view_student, name='view_student'),
    path('view_student/<int:pk>/', StudentDetailView.as_view(), name='view_student'),

]
