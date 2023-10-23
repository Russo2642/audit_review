from django.contrib import admin

from review.models import Review

from review.models import ReviewTitle


# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'created_at')
    list_display_links = ['id']
    list_filter = ('author', 'created_at')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class ReviewTitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'name', 'created_at')
    list_display_links = ['id']
    list_filter = ('author', 'created_at')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


admin.site.register(Review, ReviewAdmin)
admin.site.register(ReviewTitle, ReviewTitleAdmin)
