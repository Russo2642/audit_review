from django.db import models


class ReviewChoice(models.IntegerChoices):
    not_applicable = 0, '0 - Не преминимо'
    totally_disagree = 1, '1 - Полностью не согласен'
    disagree = 2, '2 - Не согласен'
    rather_disagree = 3, '3 - Скорее не согласен'
    rather_agree = 4, '4 - Скорее согласен'
    completely_agree = 5, '5 - Полностью согласен'


class Review(models.Model):
    author = models.ForeignKey(
        null=False,
        to='accounts.User',
        related_name='review_author',
        blank=False,
        verbose_name='Автор',
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        null=False,
        blank=False,
        max_length=300,
        verbose_name='Наименование',
    )
    block_a_1 = models.IntegerField(
        null=False,
        blank=False,
        choices=ReviewChoice.choices,
        default=ReviewChoice.not_applicable,
    )
    block_a_2 = models.IntegerField(
        null=False,
        blank=False,
        choices=ReviewChoice.choices,
        default=ReviewChoice.not_applicable,
    )
    block_a_3 = models.IntegerField(
        null=False,
        blank=False,
        choices=ReviewChoice.choices,
        default=ReviewChoice.not_applicable,
    )
    comment_block_a = models.TextField(
        max_length=3000,
        null=False,
        blank=False,
        verbose_name='Коментарии блока "Процесс Аудита"',
    )
    block_b_1 = models.IntegerField(
        null=False,
        blank=False,
        choices=ReviewChoice.choices,
        default=ReviewChoice.not_applicable,
    )
    block_b_2 = models.IntegerField(
        null=False,
        blank=False,
        choices=ReviewChoice.choices,
        default=ReviewChoice.not_applicable,
    )
    block_b_3 = models.IntegerField(
        null=False,
        blank=False,
        choices=ReviewChoice.choices,
        default=ReviewChoice.not_applicable,
    )
    block_b_4 = models.IntegerField(
        null=False,
        blank=False,
        choices=ReviewChoice.choices,
        default=ReviewChoice.not_applicable,
    )
    comment_block_b = models.TextField(
        max_length=3000,
        null=False,
        blank=False,
        verbose_name='Коментарии блока "Аудиторская команда"',
    )
    block_c_1 = models.IntegerField(
        null=False,
        blank=False,
        choices=ReviewChoice.choices,
        default=ReviewChoice.not_applicable,
    )
    block_c_2 = models.IntegerField(
        null=False,
        blank=False,
        choices=ReviewChoice.choices,
        default=ReviewChoice.not_applicable,
    )
    block_c_3 = models.IntegerField(
        null=False,
        blank=False,
        choices=ReviewChoice.choices,
        default=ReviewChoice.not_applicable,
    )
    block_c_4 = models.IntegerField(
        null=False,
        blank=False,
        choices=ReviewChoice.choices,
        default=ReviewChoice.not_applicable,
    )
    comment_block_c = models.TextField(
        max_length=3000,
        null=False,
        blank=False,
        verbose_name='Коментарии блока "Завершение аудита и отчётность"',
    )
    block_d_1 = models.IntegerField(
        null=False,
        blank=False,
        choices=ReviewChoice.choices,
        default=ReviewChoice.not_applicable,
    )
    block_d_2 = models.IntegerField(
        null=False,
        blank=False,
        choices=ReviewChoice.choices,
        default=ReviewChoice.not_applicable,
    )
    comment_block_d = models.TextField(
        max_length=3000,
        null=False,
        blank=False,
        verbose_name='Коментарии блока "Польза от объекта аудита"',
    )
    wishes = models.TextField(
        max_length=3000,
        null=True,
        blank=True,
        verbose_name='Пожелания',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления",
    )

    # @property
    # def overall_score(self):
    #     counter = 0
    #     lst = [self.block_a_1, self.block_a_2, self.block_a_3, self.block_b_1, self.block_b_2, self.block_b_3,
    #            self.block_b_4, self.block_c_1, self.block_c_2, self.block_c_3, self.block_c_4, self.block_d_1,
    #            self.block_d_2]
    #     for i in lst:
    #         counter += i
    #     return counter / len(lst)

    @property
    def block_a_sum(self):
        lst = [self.block_a_1, self.block_a_2, self.block_a_3]
        return round(sum(lst) / len(lst), 2)

    @property
    def block_b_sum(self):
        lst = [self.block_b_1, self.block_b_2, self.block_b_3, self.block_b_4]
        return round(sum(lst) / len(lst), 2)

    @property
    def block_c_sum(self):
        lst = [self.block_c_1, self.block_c_2, self.block_c_3, self.block_c_4]
        return round(sum(lst) / len(lst), 2)

    @property
    def block_d_sum(self):
        lst = [self.block_d_1, self.block_d_2]
        return round(sum(lst) / len(lst), 2)

    @property
    def total_for_all_blocks(self):
        total = self.block_a_sum + self.block_b_sum + self.block_c_sum + self.block_d_sum
        return round(total / 4, 2)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f"Отзыв {self.author} за {self.created_at}"
