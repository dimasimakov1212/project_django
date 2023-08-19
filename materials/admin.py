from django.contrib import admin

from materials.models import Material


# admin.site.register(Student)


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('material_title', 'views_count', 'is_published',)
    list_filter = ('material_title',)
    search_fields = ('material_title', 'last_name',)
