# Generated by Django 4.1.7 on 2023-11-24 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Наименование')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_title', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Наименование проверки',
                'verbose_name_plural': 'Наименования проверок',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Наименование')),
                ('block_a_1', models.IntegerField(choices=[(0, '0 - Не преминимо'), (1, '1 - Полностью не согласен'), (2, '2 - Не согласен'), (3, '3 - Скорее не согласен'), (4, '4 - Скорее согласен'), (5, '5 - Полностью согласен')], default=0)),
                ('block_a_2', models.IntegerField(choices=[(0, '0 - Не преминимо'), (1, '1 - Полностью не согласен'), (2, '2 - Не согласен'), (3, '3 - Скорее не согласен'), (4, '4 - Скорее согласен'), (5, '5 - Полностью согласен')], default=0)),
                ('block_a_3', models.IntegerField(choices=[(0, '0 - Не преминимо'), (1, '1 - Полностью не согласен'), (2, '2 - Не согласен'), (3, '3 - Скорее не согласен'), (4, '4 - Скорее согласен'), (5, '5 - Полностью согласен')], default=0)),
                ('comment_block_a', models.TextField(max_length=3000, verbose_name='Коментарии блока "Процесс Аудита"')),
                ('block_b_1', models.IntegerField(choices=[(0, '0 - Не преминимо'), (1, '1 - Полностью не согласен'), (2, '2 - Не согласен'), (3, '3 - Скорее не согласен'), (4, '4 - Скорее согласен'), (5, '5 - Полностью согласен')], default=0)),
                ('block_b_2', models.IntegerField(choices=[(0, '0 - Не преминимо'), (1, '1 - Полностью не согласен'), (2, '2 - Не согласен'), (3, '3 - Скорее не согласен'), (4, '4 - Скорее согласен'), (5, '5 - Полностью согласен')], default=0)),
                ('block_b_3', models.IntegerField(choices=[(0, '0 - Не преминимо'), (1, '1 - Полностью не согласен'), (2, '2 - Не согласен'), (3, '3 - Скорее не согласен'), (4, '4 - Скорее согласен'), (5, '5 - Полностью согласен')], default=0)),
                ('block_b_4', models.IntegerField(choices=[(0, '0 - Не преминимо'), (1, '1 - Полностью не согласен'), (2, '2 - Не согласен'), (3, '3 - Скорее не согласен'), (4, '4 - Скорее согласен'), (5, '5 - Полностью согласен')], default=0)),
                ('comment_block_b', models.TextField(max_length=3000, verbose_name='Коментарии блока "Аудиторская команда"')),
                ('block_c_1', models.IntegerField(choices=[(0, '0 - Не преминимо'), (1, '1 - Полностью не согласен'), (2, '2 - Не согласен'), (3, '3 - Скорее не согласен'), (4, '4 - Скорее согласен'), (5, '5 - Полностью согласен')], default=0)),
                ('block_c_2', models.IntegerField(choices=[(0, '0 - Не преминимо'), (1, '1 - Полностью не согласен'), (2, '2 - Не согласен'), (3, '3 - Скорее не согласен'), (4, '4 - Скорее согласен'), (5, '5 - Полностью согласен')], default=0)),
                ('block_c_3', models.IntegerField(choices=[(0, '0 - Не преминимо'), (1, '1 - Полностью не согласен'), (2, '2 - Не согласен'), (3, '3 - Скорее не согласен'), (4, '4 - Скорее согласен'), (5, '5 - Полностью согласен')], default=0)),
                ('block_c_4', models.IntegerField(choices=[(0, '0 - Не преминимо'), (1, '1 - Полностью не согласен'), (2, '2 - Не согласен'), (3, '3 - Скорее не согласен'), (4, '4 - Скорее согласен'), (5, '5 - Полностью согласен')], default=0)),
                ('comment_block_c', models.TextField(max_length=3000, verbose_name='Коментарии блока "Завершение аудита и отчётность"')),
                ('block_d_1', models.IntegerField(choices=[(0, '0 - Не преминимо'), (1, '1 - Полностью не согласен'), (2, '2 - Не согласен'), (3, '3 - Скорее не согласен'), (4, '4 - Скорее согласен'), (5, '5 - Полностью согласен')], default=0)),
                ('block_d_2', models.IntegerField(choices=[(0, '0 - Не преминимо'), (1, '1 - Полностью не согласен'), (2, '2 - Не согласен'), (3, '3 - Скорее не согласен'), (4, '4 - Скорее согласен'), (5, '5 - Полностью согласен')], default=0)),
                ('comment_block_d', models.TextField(max_length=3000, verbose_name='Коментарии блока "Польза от объекта аудита"')),
                ('wishes', models.TextField(blank=True, max_length=3000, null=True, verbose_name='Пожелания')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_author', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ('-created_at',),
            },
        ),
    ]
