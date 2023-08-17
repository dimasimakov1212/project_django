from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from pytils.translit import slugify

from materials.models import Material


class MaterialCreateView(CreateView):
    """
    Выводит форму создания мариала
    """
    model = Material
    fields = ('material_title', 'material_body',)
    success_url = reverse_lazy('materials:list')

    def form_valid(self, form):
        """
        Реализует создание Slug — человекопонятный URL
        """
        if form.is_valid():
            new_material = form.save()
            new_material.slug = slugify(new_material.material_title)
            new_material.save()
            
        return super().form_valid(form)


class MaterialListView(ListView):
    """
    Выводит информацию о материалах
    """
    model = Material

    def get_queryset(self, *args, **kwargs):
        """
        Выводит список материалов только опубликованных
        """
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)

        return queryset


class MaterialDetailView(DetailView):
    """
    Выводит информаццию об одном, выбранном на главной странице, материале
    """
    model = Material
    # template_name = 'materials/material_detail.html'

    def get_object(self, queryset=None):
        """
        Считает количество просмотров карточки материала
        """
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()

        return self.object


class MaterialUpdateView(UpdateView):
    """
    Выводит форму редактирования материала
    """
    model = Material
    fields = ('material_title', 'material_body',)
    # success_url = reverse_lazy('materials:list')

    def form_valid(self, form):
        """
        Реализует создание Slug — человекопонятный URL
        """
        if form.is_valid():
            new_material = form.save()
            new_material.slug = slugify(new_material.material_title)
            new_material.save()

        return super().form_valid(form)

    def get_success_url(self):
        """
        Получает адрес перенаправления после редактирования материала
        """
        return reverse('materials:view', args=[self.kwargs.get('pk')])


class MaterialDeleteView(DeleteView):
    """
    Выводит форму удаления материала
    """
    model = Material
    success_url = reverse_lazy('materials:list')
