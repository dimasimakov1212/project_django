from django.db import models


class Material(models.Model):
    material_title = models.CharField(max_length=150, verbose_name='название')
    material_body = models.TextField(verbose_name='содержимое')

    def __str__(self):
        return self.material_title

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'
