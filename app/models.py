from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=80, verbose_name='Product')
    content = models.TextField(null=True, blank=True, verbose_name='Description')
    price = models.FloatField(null=True, blank=True, verbose_name='Price')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Publication date')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Rubric')
    image = models.ImageField(blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Posts'
        verbose_name = 'Post'
        ordering = '-published',

class Rubric(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='name')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Rubrics'
        verbose_name = 'Rubric'
        ordering = ['name']