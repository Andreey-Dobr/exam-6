from django.db import models

STATUS= [
    ('active','Активно'),
    ('blocked','Заблокировано')

]


class Article(models.Model):
    author = models.CharField(max_length=40, null=True, blank=True, default='Unknown', verbose_name='Автор')
    email = models.EmailField(max_length=200, null=True, blank=True, verbose_name='Почта')
    text = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Текст')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    status = models.CharField(max_length=25, choices=STATUS, default='active', verbose_name='статус')

    def __str__(self):
        return f'{self.author} - {self.email}'
