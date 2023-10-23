from django.contrib.auth.models import AbstractUser
from django.db import models
from review.models.review_title import ReviewTitle


class DepartmentChoice(models.TextChoices):
    SVA = 'SVA', 'СВА'
    DUKD = 'DUKD', 'ДУКД'
    DPT = 'DPT', 'ДПТ'


class ActivateChoice(models.TextChoices):
    NOT_ACTIVE = 'NOT_ACTIVE', 'Не активно'
    ACTIVE = 'ACTIVE', 'Активно'


class User(AbstractUser):
    username = models.CharField(
        max_length=512,
        null=False,
        blank=False,
        unique=True,
        verbose_name='Логин',
    )
    department = models.CharField(
        max_length=256,
        null=False,
        choices=DepartmentChoice.choices,
        default=DepartmentChoice.SVA,
        verbose_name='Департамент',
    )
    activating = models.CharField(
        max_length=256,
        null=False,
        choices=ActivateChoice.choices,
        default=ActivateChoice.NOT_ACTIVE,
        verbose_name='Статус',
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    # @property
    # def overall_score_for_the_quarter(self):
    #     counter = 0
    #     authors = []
    #     for i in self.review.all():
    #         authors.append(i.author)
    #         counter += (i.block_a_sum + i.block_b_sum + i.block_c_sum + i.block_d_sum) / 4
    #     try:
    #         return round(counter / len(authors), 2)
    #     except ZeroDivisionError:
    #         return 0

    def __str__(self):
        return self.username

    def update_active(self):
        if self.activating == ActivateChoice.ACTIVE:
            self.activating = ActivateChoice.NOT_ACTIVE
        else:
            self.activating = ActivateChoice.ACTIVE
        self.save()
