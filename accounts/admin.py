from accounts.models import User
from django.contrib import admin


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'department', 'activating')
    list_display_links = ['id']
    list_filter = ('department', 'activating')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


admin.site.register(User, UserProfileAdmin)
