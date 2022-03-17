# Generated by Django 4.0.3 on 2022-03-16 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=50, verbose_name='Введите заголовок')),
                ('article_text', models.TextField(verbose_name='Введите текст')),
            ],
        ),
    ]