import logging

from django.contrib import admin
from me2ushop import admin as admin_register
from me2ushop.admin import make_active, make_inactive
from mptt.admin import DraggableMPTTAdmin

from .models import Category, Department

logger = logging.getLogger(__name__)


class DepartmentAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'is_active', 'created', 'modified',)
    list_display_links = ('indented_title',)
    actions = [make_active, make_inactive]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'description', 'is_active', 'created_at', 'updated_at',)
    list_display_links = ('category_name',)
    list_per_page = 20
    ordering = ['category_name']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at',
               'updated_at',)
    # sets up slug to be generated from category name
    prepopulated_fields = {'slug': ('category_name',)}

    fieldsets = (
        (
            None, {
                'fields': ('category_name',)
            }
        ),
    )

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.readonly_fields
        return list(self.readonly_fields) + ['slug', 'category_name']

    def get_prepopulated_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.prepopulated_fields
        else:
            return {}


# main_admin = OwnersAdminSite()


admin.site.register(Category, CategoryAdmin)
# admin.site.register(Department, DepartmentAdmin)
admin.site.register(Department, DepartmentAdmin)
# admin.site.register(, DepartmentAdmin)

admin_register.main_admin.register(Category, CategoryAdmin)
