from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from materials.models import Material


class MaterialCreateView(CreateView):
    """
    Выводит форму создания мариала
    """
    model = Material
    fields = ('material_title', 'material_body',)
    success_url = reverse_lazy('main:test_html')


class MaterialDetailView(DetailView):
    """
    Выводит информаццию об одном, выбранном на главной странице, студенте вместо функции view_student
    """
    model = Material
    template_name = 'main/view_student.html'