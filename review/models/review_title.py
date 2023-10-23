from django.db import models


class ReviewTitle(models.Model):
    author = models.ForeignKey(
        null=True,
        to='accounts.User',
        related_name='author_title',
        blank=True,
        verbose_name='Автор',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        null=False,
        blank=False,
        max_length=300,
        verbose_name='Наименование',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления",
    )

    class Meta:
        verbose_name = 'Наименование проверки'
        verbose_name_plural = 'Наименования проверок'

    def __str__(self):
        return f'{self.author} - {self.name}'
