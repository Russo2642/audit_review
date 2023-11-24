from accounts.models import User
from django.contrib import admin

from accounts.models.user import Department


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'get_department', 'activating')
    list_display_links = ['id']
    list_filter = ('department', 'activating')

    def get_department(self, obj):
        if obj.department:
            return obj.department.name
        return obj

    get_department.department = 'department'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ['id']
    list_filter = ('name', )

    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'


admin.site.register(User, UserProfileAdmin)
admin.site.register(Department, DepartmentAdmin)
