from django.urls import path, include
from django.views.decorators.cache import cache_page

from main.apps import MainConfig
from main.views import contact, StudentDetailView, StudentListView, StudentCreateView, toggle_activity, \
    StudentUpdateView, StudentDeleteView

app_name = MainConfig.name

urlpatterns = [
    # path('', index_2, name='test_html'),
    path('', cache_page(60)(StudentListView.as_view()), name='test_html'),  # кэшируется контроллер всей страницы
    path('contact/', contact, name='contact'),
    # path('view_student/<int:pk>/', view_student, name='view_student'),
    path('view_student/<int:pk>/', StudentDetailView.as_view(), name='view_student'),
    path('create/', StudentCreateView.as_view(), name='create_student'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='update_student'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='delete_student'),
    path('activity/<int:pk>/', toggle_activity, name='toggle_activity'),
]
