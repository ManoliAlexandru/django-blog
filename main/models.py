from email.mime import image
from tabnanny import verbose
from django.db import models

class Article(models.Model):
  title = models.CharField('Введите заголовок', max_length = 50)
  text = models.TextField('Введите текст')

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = 'Статья'
    verbose_name_plural = 'Статьи'