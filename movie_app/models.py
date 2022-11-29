from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Director(models.Model):
    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'
    name = models.CharField(max_length=255, verbose_name='Имя')

    def __str__(self):
        return self.name


class Movie(models.Model):
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    duration = models.IntegerField(help_text='Длительность в минутах', verbose_name='Длительность')
    director = models.ForeignKey(Director, on_delete=models.SET_DEFAULT, default='Неизвестно', verbose_name='Режиссер')

    def __str__(self):
        return self.title


class Review(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.TextField(verbose_name='Текст')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='Фильм')

    def __str__(self):
        if len(self.text) <= 50:
            return (self.author.username if self.author is not None else 'Anonymous') + ', ' + self.text + '; ' + self.movie.title
        return (self.author.username if self.author is not None else 'Anonymous') + ', ' + self.text[0:50] + '...;  ' + self.movie.title