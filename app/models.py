from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=80, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Обьявления'
        verbose_name = 'Обьявление'
        ordering = '-published',

class Rubric(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='Название')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']

class Author(models.Model):
    author = models.CharField(max_length=100, blank=True, null=True)