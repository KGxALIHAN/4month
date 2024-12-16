from django.db import models

class BookModels(models.Model):
    GENRE = (
        ('Ужасы', 'Ужасы'),
        ('Комедия', 'Комедия'),
        ('Приключения', 'Приключения')
    )
    image = models.ImageField(upload_to='films/', verbose_name='Загрузите фото книги')
    title = models.CharField(max_length=100, verbose_name='укажите название книги')
    description = models.TextField(verbose_name='Укажите описание', blank=True)
    price = models.FloatField(verbose_name='укажите цену на книгу', default=10)
    created_at = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=100, choices=GENRE, default='Комедия')
    time_watch = models.TimeField(verbose_name='Укажите количество глав', blank=True)
    director = models.CharField(max_length=100, verbose_name='укажите автора', default='Иван Иванов')

    class Meta:
        verbose_name = 'книги'
        verbose_name_plural = 'книги'
    def __str__(self):
        return self.title