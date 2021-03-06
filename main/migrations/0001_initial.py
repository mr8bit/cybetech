# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-29 14:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Категория проекта')),
            ],
            options={
                'verbose_name_plural': 'Категории',
                'verbose_name': 'Категория',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=400, verbose_name='Почта')),
                ('name', models.CharField(max_length=400, verbose_name='Имя')),
                ('name_company', models.CharField(max_length=400, verbose_name='Название компании')),
                ('massage', models.TextField(verbose_name='Сообщение')),
            ],
            options={
                'verbose_name_plural': 'Обращения к нам',
                'verbose_name': 'Обращения к нам',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=100, verbose_name='Телефон')),
                ('address', models.CharField(max_length=100, verbose_name='Адресс')),
                ('telegram', models.CharField(max_length=300, verbose_name='Ссылкка на чат в телеграмме')),
                ('email', models.EmailField(default='', max_length=300, verbose_name='Почта')),
            ],
            options={
                'verbose_name_plural': 'Наши контакты',
                'verbose_name': 'Наши контакты',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(max_length=300, verbose_name='Наименование заказа')),
                ('email', models.CharField(max_length=400, verbose_name='Почта')),
                ('name', models.CharField(max_length=400, verbose_name='Имя')),
                ('name_company', models.CharField(max_length=400, verbose_name='Название компании')),
                ('massage', models.TextField(verbose_name='Сообщение')),
            ],
            options={
                'verbose_name_plural': 'Заказы',
                'verbose_name': 'Заказ',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название')),
                ('tagline', models.CharField(max_length=300, verbose_name='Слоган')),
                ('img', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('cssClass', models.CharField(max_length=300, verbose_name='Css класс')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name_plural': 'Проекты',
                'verbose_name': 'Проект',
            },
        ),
        migrations.CreateModel(
            name='RecentlyInWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=300, verbose_name='Название')),
                ('img', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('link', models.CharField(max_length=400, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name_plural': 'В работе',
                'verbose_name': 'В работе',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('link', models.CharField(max_length=400, verbose_name='Ссылка')),
                ('icon_name', models.CharField(max_length=300, verbose_name='Css Иконка')),
                ('cssClass', models.CharField(max_length=300, verbose_name='Css класс')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='main.Contacts')),
            ],
            options={
                'verbose_name_plural': 'Соц. сети',
                'verbose_name': 'Соц. сети',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Тип Проекта')),
            ],
            options={
                'verbose_name_plural': 'Типы',
                'verbose_name': 'Тип',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Type', verbose_name='Тип'),
        ),
    ]
