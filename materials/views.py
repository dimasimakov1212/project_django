from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from materials.models import Material


class MaterialCreateView(CreateView):
    """
    Выводит форму создания мариала
    """
    model = Material
    fields = ('material_title', 'material_body',)
    success_url = reverse_lazy('materials:list')


class MaterialListView(ListView):
    """
    Выводит информацию о материале
    """
    model = Material


class MaterialDetailView(DetailView):
    """
    Выводит информаццию об одном, выбранном на главной странице, студенте вместо функции view_student
    """
    model = Material
    template_name = 'materials/view_material.html'
