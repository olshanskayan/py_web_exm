from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):

    CONDITIONS = (
        (0, 'Активно'),
        (1, 'Отложено'),
        (2, 'Выполнено'),
    )

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    message = models.TextField(default='', verbose_name='Текст')
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    public = models.BooleanField(default=False, verbose_name='Опубликовать')
    condition = models.IntegerField(default=0, choices=CONDITIONS, verbose_name='Статус состояния')
    mark = models.BooleanField(default=False, verbose_name='Публичная')
    author = models.ForeignKey(User, related_name='authors', on_delete=models.PROTECT, verbose_name='Автор')

    def __str__(self):
        return self.title

